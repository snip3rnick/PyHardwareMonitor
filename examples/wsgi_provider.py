# coding: utf-8

import json
import time
import socket
from threading import Timer, Lock
from typing import Iterable, List
from wsgiref import simple_server
from HardwareMonitor.Util import OpenComputer, ToBuiltinTypes
from HardwareMonitor.Hardware import HardwareType, SensorType, IComputer, IHardware, ISensor


# ------------------------------------------------------------------------------
def getattr_items(obj):
    def object_getattr(attr):
        try:    return getattr(obj, attr)
        except: pass
    return zip(dir(obj), map(object_getattr, dir(obj)))

HardwareTypeString = dict((v, a) for (a, v) in getattr_items(HardwareType) if type(v) in (int, HardwareType))
SensorTypeString   = dict((v, a) for (a, v) in getattr_items(SensorType)   if type(v) in (int, SensorType))

SensorTypeStringPlurals = {
    SensorType.Voltage: "Voltages",
    SensorType.Current: "Currents",
    SensorType.Clock: "Clocks",
    SensorType.Load: "Loads",
    SensorType.Temperature: "Temperatures",
    SensorType.Fan: "Fans",
    SensorType.Level: "Levels",
    SensorType.Power: "Powers",
    SensorType.Frequency: "Frequencies",
}

SensorTypeUnitFormat = {
    SensorType.Voltage: "{:.3f} V",
    SensorType.Current: "{:.3f} A",
    SensorType.Clock: "{:.1f} MHz",
    SensorType.Load: "{:.1f} %",
    SensorType.Temperature: "{:.1f} °C",
    SensorType.Fan: "{:d} RPM",
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
    SensorType.Energy: "{:d} mWh",
}


# ------------------------------------------------------------------------------
class NodeFormatter():
    _counter = 0
    def getId(self):
        node_id = self._counter
        self._counter += 1
        return node_id

    def _makeNode(self, Text, Min="", Value="", Max="", ImageURL="", **kwargs):
        return dict(id=self.getId(), Text=Text, Min=Min, Value=Value, Max=Max,
                    ImageURL=ImageURL, Children=[], **kwargs)

    def groupSensors(self, sensors: Iterable[ISensor]) -> List[List[ISensor]]:
        groups = {}
        for sensor in sensors:
            group = groups[sensor.SensorType] = groups.get(sensor.SensorType, [])
            group.append(sensor)
        return list(groups.values())

    def makeSensorGroupNode(self, sensors: List[ISensor]):
        sensor_type = sensors[0].SensorType
        type_str    = SensorTypeString[sensor_type]
        unit_format = SensorTypeUnitFormat.get(sensor_type, "{}")
        def makeSensorNode(sensor: ISensor):
            min_str = unit_format.format(sensor.Min or 0)
            val_str = unit_format.format(sensor.Value or 0)
            max_str = unit_format.format(sensor.Max or 0)
            return self._makeNode(sensor.Name, Min=min_str, Value=val_str, Max=max_str, Type=type_str,
                                  SensorId=sensor.Identifier.ToString())

        group_node = self._makeNode(SensorTypeStringPlurals.get(sensor_type, type_str))
        group_node["Children"].extend(map(makeSensorNode, sensors))
        return group_node

    def makeHardwareNode(self, hardware: IHardware):
        hardware_type = HardwareTypeString[hardware.HardwareType]
        hardware_node = self._makeNode(hardware.Name, Type=hardware_type)
        hardware_node["Children"].extend(map(self.makeSensorGroupNode, self.groupSensors(hardware.Sensors)))
        hardware_node["Children"].extend(map(self.makeHardwareNode, hardware.SubHardware))
        return hardware_node

    def buildNodeTree(self, computer: IComputer):
        self._counter = 0
        root_node = self._makeNode("Sensor")
        computer_node = self._makeNode(socket.gethostname())

        root_node["Children"].append(computer_node)
        computer_node["Children"].extend(map(self.makeHardwareNode, computer.Hardware))
        return root_node



# ------------------------------------------------------------------------------
class IndefiniteTimer(Timer):
    def start(self):
        self.daemon = True
        super().start()
        return self

    def run(self):
        delay = self.interval
        while not self.finished.wait(delay):
            start_time = time.perf_counter()
            self.function(*self.args, **self.kwargs)
            delay = max(0, self.interval - (time.perf_counter() - start_time))


# ------------------------------------------------------------------------------
class SensorApp():
    def __init__(self, port=8085, interval=1.0):
        self.interval = interval
        self.mutex    = Lock()
        self.computer = OpenComputer(all=True, time_window=interval)
        self.timer    = IndefiniteTimer(interval, self.update).start()
        self.http     = simple_server.make_server('', port, self.handler)

    @property
    def port(self):
        return self.http.server_port

    def update(self):
        with self.mutex:
            self.computer.Update()

    def getSensors(self):
        with self.mutex:
            return NodeFormatter().buildNodeTree(self.computer)
            # return ToBuiltinTypes(self.computer.Hardware)

    def serve(self):
        self.http.serve_forever()

    def close(self):
        self.timer.cancel()
        self.http.shutdown()

    def handler(self, environ, respond):
        if environ['PATH_INFO'].lower() == "/data.json":
            json_str = json.dumps(self.getSensors(), ensure_ascii=False)
            respond('200 OK', [('Content-Type', 'application/json')])
            return [json_str.encode("utf-8")]
        else:
            respond('404 Not Found', [('Content-Type', 'application/json')])
            return [b'not found']


# ------------------------------------------------------------------------------
def main():
    print(f"Loading devices and sensors...")
    app = SensorApp()
    print(f"Serving on 'http://localhost:{app.port}/data.json', press 'ctrl + C' to stop")
    try:
        app.serve()
    except KeyboardInterrupt:
        app.close()

if __name__ == "__main__":
    main()
