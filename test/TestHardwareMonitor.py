# Test script enumerating all hardware components and listing available sensors

import sys, os
sys.path.insert(0, os.path.abspath(__file__ + "/../.."))


from HardwareMonitor.Hardware import Computer, IVisitor, IComputer, IHardware, IParameter, ISensor
from HardwareMonitor.Util import SensorValueToString


class UpdateVisitor(IVisitor):
    __namespace__ = "TestHardwareMonitor"
    def VisitComputer(self, computer: IComputer):
        computer.Traverse(self)

    def VisitHardware(self, hardware: IHardware):
        hardware.Update()
        for subHardware in hardware.SubHardware:
            subHardware.Update()

    def VisitParameter(self, parameter: IParameter):
        pass

    def VisitSensor(self, sensor: ISensor):
        pass


computer = Computer()
computer.IsMotherboardEnabled = True
computer.IsControllerEnabled = True
computer.IsCpuEnabled = True
computer.IsGpuEnabled = True
computer.IsBatteryEnabled = True
computer.IsMemoryEnabled = True
computer.IsNetworkEnabled = True
computer.IsStorageEnabled = True

computer.Open()
computer.Accept(UpdateVisitor())

for hardware in computer.Hardware:
    print(f"Hardware: {hardware.Name}")
    for subhardware  in hardware.SubHardware:
        print(f"\tSubhardware: {subhardware.Name}")
        for sensor in subhardware.Sensors:
            print(f"\t\tSensor: {sensor.Name}, value: {SensorValueToString(sensor.Value, sensor.SensorType)}")
    for sensor in hardware.Sensors:
        print(f"\tSensor: {sensor.Name}, value: {SensorValueToString(sensor.Value, sensor.SensorType)}")

computer.Close()
