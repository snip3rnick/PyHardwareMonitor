import sys, os

sys.path.insert(0, os.path.abspath(__file__ + "/../.."))

from HardwareMonitor import Hardware

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
    print(hardware.Name)
    print(hardware.GetReport())

c.Close()
