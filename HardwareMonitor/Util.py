
from typing import Any, Dict

import HardwareMonitor
from HardwareMonitor.Hardware import Computer, IVisitor, IComputer, IHardware, IParameter, ISensor
from System.Collections.Generic import IList, IDictionary


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
class UpdateVisitor(IVisitor):
    __namespace__ = "HardwareMonitor.Util"
    def VisitComputer(self, computer: IComputer):
        computer.Traverse(self);

    def VisitHardware(self, hardware: IHardware):
        hardware.Update()
        for subHardware in hardware.SubHardware:
            subHardware.Update()

    def VisitParameter(self, parameter: IParameter):
        pass

    def VisitSensor(self, sensor: ISensor):
        pass


# ------------------------------------------------------------------------------
def OpenComputer(**settings) -> Computer:
    computer = Computer()
    attr_filter = lambda attr: attr.startswith("Is") and attr.endswith("Enabled")
    for attr in filter(attr_filter, dir(computer)):
        key = attr[2:-7].lower()
        setattr(computer, attr, bool(settings.get(key, settings.get("all", False))))

    computer.Open()
    computer.Accept(UpdateVisitor())

    return computer


# ------------------------------------------------------------------------------
def ToBuiltinTypes(obj, visited=set(), exclude=["Parameters"]):
    # Return 'primitive' python types as such
    if type(obj) in (str, bytes, bool, int, float, tuple, list, dict, set):
        return obj
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
            return list(ToBuiltinTypes(o, visited, exclude) for o in obj)
        if IsInstanceOfInterface(obj, IDictionary):
            return dict((k, ToBuiltinTypes(obj.get_Item(k), visited, exclude)) for k in list(obj))
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
                # Simple check to skip methods
                if not callable(val):
                    val_reduced = ToBuiltinTypes(val, visited, exclude)
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
