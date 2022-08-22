import sys, os

sys.path.insert(0, os.path.abspath(__file__ + "/../.."))

from HardwareMonitor import Hardware

def VisitHardware(hardware: Hardware.IHardware):
    hardware.Update()
    for subHardware in hardware.SubHardware:
        subHardware.Update()


c = Hardware.Computer()
c.IsMotherboardEnabled = True
c.IsControllerEnabled = True
c.IsCpuEnabled = True
c.IsGpuEnabled = True
c.IsBatteryEnabled = True
c.IsMemoryEnabled = True
c.IsNetworkEnabled = True
c.IsStorageEnabled = True

c.Open()

for hardware in c.Hardware:
    print("-" * 80)
    VisitHardware(hardware)
    print(f"Hardware: {hardware.Name}")
    for subhardware  in hardware.SubHardware:
        print(f"\tSubhardware: {subhardware.Name}")
        for sensor in subhardware.Sensors:
            print(f"\t\tSensor: {sensor.Name}, value: {sensor.Value}")
    for sensor in hardware.Sensors:
        print(f"\tSensor: {sensor.Name}, value: {sensor.Value}")

c.Close()
