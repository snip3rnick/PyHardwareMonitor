from __future__ import annotations
import logging
from typing import Dict, Iterable, List

import HardwareMonitor
from HardwareMonitor.Hardware import Computer, IVisitor, IComputer, IHardware, IParameter, ISensor, HardwareType, SensorType
from System.Collections.Generic import IList, IDictionary

logger = logging.getLogger("PyHardwareMonitor")

# ------------------------------------------------------------------------------
def _get_name_to_type(obj):
    def object_getattr(attr):
        try:    return getattr(obj, attr)
        except: pass
    result = {}
    for (a, v) in zip(dir(obj), map(object_getattr, dir(obj))):
        if type(v) in (int, obj):
            result[v] = result[int(v)] = a
    return result

HardwareTypeString: Dict[HardwareType|int, str] = _get_name_to_type(HardwareType)
SensorTypeString:   Dict[SensorType  |int, str] = _get_name_to_type(SensorType)

SensorTypeUnitFormatter = {
    SensorType.Voltage: "{:.3f} V",
    SensorType.Current: "{:.3f} A",
    SensorType.Clock: "{:.1f} MHz",
    SensorType.Load: "{:.1f} %",
    SensorType.Temperature: "{:.1f} °C",
    SensorType.Fan: "{:.0f} RPM",
    SensorType.Flow: "{:.1f} L/h",
    SensorType.Control: "{:.1f} %",
    SensorType.Level: "{:.1f} %",
    SensorType.Power: "{:.1f} W",
    SensorType.Data: "{:.1f} GB",
    SensorType.SmallData: "{:.1f} MB",
    SensorType.Factor: "{:.3f}",
    SensorType.Frequency: "{:.1f} Hz",
    SensorType.Throughput: "{:.1f} B/s",
    SensorType.TimeSpan: "{}",
    SensorType.Energy: "{:.0f} mWh",
}

def SensorValueToString(value: float, type: SensorType) -> str:
    return SensorTypeUnitFormatter.get(type, "{}").format(value or 0)


def GroupSensorsByType(sensors: Iterable[ISensor]) -> List[List[ISensor]]:
    groups = {}
    for sensor in sensors:
        group = groups[sensor.SensorType] = groups.get(sensor.SensorType, [])
        group.append(sensor)
    return list(groups.values())


# ------------------------------------------------------------------------------
_generic_type_cache = {}


def IsInstanceOfInterface(obj, interface):
    if not hasattr(obj, "GetType"):
        return False
    try:
        obj_type = obj.GetType()
        if obj_type in _generic_type_cache:
            return any(cmp == interface for cmp in _generic_type_cache[obj_type])
        ifaces = list(i for i in obj.GetType().GetInterfaces() if i.IsGenericType)
        cache  = _generic_type_cache[obj_type] = set()
        for iface in ifaces:
            cache.add(iface.GetGenericTypeDefinition())
        return any(cmp == interface for cmp in cache)
    except:
        pass
    return False


# ------------------------------------------------------------------------------
_UPDATE_WARNING_CACHE = set()
def UpdateHardwareSafe(hardware: IHardware):
    try:
        hardware.Update()
    except:
        if hardware.Identifier not in _UPDATE_WARNING_CACHE:
            logger.warning(f"Unable to update HardwareMonitor sensors for {hardware.Identifier} ('{hardware.Name}')")
            _UPDATE_WARNING_CACHE.add(hardware.Identifier)


# ------------------------------------------------------------------------------
class UpdateVisitor(IVisitor):
    __namespace__ = "HardwareMonitor.Util"
    def __init__(self, time_window=1.0):
        super().__init__()
        self.time_window = time_window

    def VisitComputer(self, computer: IComputer):
        computer.Traverse(self);

    def VisitHardware(self, hardware: IHardware):
        UpdateHardwareSafe(hardware)
        for subHardware in hardware.SubHardware:
            UpdateHardwareSafe(subHardware)

    def VisitParameter(self, parameter: IParameter):
        pass

    def VisitSensor(self, sensor: ISensor):
        sensor.ValuesTimeWindow = self.time_window


# ------------------------------------------------------------------------------
class PyComputer(Computer):
    def __init__(self, time_window=1.0, **settings):
        super().__init__()
        attr_filter = lambda attr: attr.startswith("Is") and attr.endswith("Enabled")
        for attr in filter(attr_filter, dir(self)):
            key = attr[2:-7].lower()
            setattr(self, attr, bool(settings.get(key, settings.get("all", False))))
        self._visitor = UpdateVisitor(time_window)

    def Update(self):
        self.Open()
        self.Accept(self._visitor)
        return self

    def __enter__(self):
        self.Open()
        self.Accept(self._visitor)
        return self

    def __exit__(self, *args):
        self.Close()

    def __del__(self):
        try:    self.Close()
        except: pass


# ------------------------------------------------------------------------------
def OpenComputer(**settings) -> PyComputer:
    computer = PyComputer(**settings)
    return computer.Update()


# ------------------------------------------------------------------------------
def ToBuiltinTypes(obj, exclude=["Parameters", "Values"]):
    def process_object(obj):
        # Return 'primitive' python types as such
        if type(obj) in (str, bytes, bool, int, float):
            return obj
        elif type(obj) in (list, tuple, set):
            return list(map(process_object, obj))
        elif type(obj) in (dict,):
                return dict((k, process_object(v)) for k,v in obj.items())
        # Handle .NET objects
        if hasattr(obj, "GetType"):
            # Return enums as the string representation of the value
            if obj.GetType().IsEnum:
                return obj.ToString()
            # Prevent recursion within HardwareMonitor objects
            if obj in visited:
                return None
            visited.add(obj)
            # Convert lists and dictionaries to python objects
            if obj.GetType().IsArray or IsInstanceOfInterface(obj, IList):
                return list(map(process_object, obj))
            if IsInstanceOfInterface(obj, IDictionary):
                return dict((k, process_object(obj.get_Item(k))) for k in list(obj))
            # Handle objects from the 'HardwareMonitor.Hardware' namespace
            if obj.__class__.__module__.startswith(HardwareMonitor.ASSEMBLY_NAME):
                cls_name = obj.__class__.__name__
                if cls_name[:2].isupper() and cls_name[0] == "I":
                    cls_name = cls_name[1:]
                obj_dict = {}
                # Iterate over all "public" members of the object
                for attr in [a for a in dir(obj) if not a.startswith("_")]:
                    if attr in exclude or attr.startswith("IsDefault"):
                        continue
                    val = getattr(obj, attr)
                    val_reduced = process_object(val)
                    if val_reduced is None or val_reduced == [None]:
                        continue
                    elif val_reduced or type(val_reduced) is not dict:
                        obj_dict[attr] = val_reduced
                if not obj_dict:
                    return None
                # Add the class name to allow for easy filtering
                result = {"Type": cls_name}
                result.update(obj_dict)
                return result
        return None
    visited = set()
    return process_object(obj)
