# PyHardwareMonitor

Python Harware Monitor is a thin package layer for [`LibreHardwareMonitorLib`](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor) using [`pythonnet`](https://github.com/pythonnet/pythonnet). 
Libre Hardware Monitor, a fork of Open Hardware Monitor, is free software that can monitor the temperature sensors, fan speeds, voltages, load and clock speeds of your computer. 
This package is mostly auto generated using the [`pythonstubs`](https://github.com/mcneel/pythonstubs) generator tool for .NET libraries.
Scripts for generating, altering and extending package resources are located in the [scripts folder](https://github.com/snip3rnick/PyHardwareMonitor/tree/main/scripts).

The purpose of this layer is the ability to provide extensive typing information and additional utilities around the LibreHardwareMonitorLib.

> **Note:** Python must have **admin privileges** for `HardwareMonitor` to be able to access all available sensors properly!


## Prerequisites
- Python 3.6+
  - pythonnet
  - .NET 4.7
- PawnIO (for system sensors)


## Installation

Install from PyPi directly
```
pip3 install HardwareMonitor
```

or install locally from source

```
git clone https://github.com/snip3rnick/PyHardwareMonitor
cd PyHardwareMonitor
pip3 install .
```

### PawnIO Input/Output Driver

For many system sensors (eg. motherboard) it is required to install the [PawnIO driver](https://pawnio.eu/).  
The driver can be installed using ``winget``
```
winget install PawnIO
```

Alternatively you may download the latest version from the [GitHub release](https://github.com/namazso/PawnIO.Setup/releases/latest/download/PawnIO_setup.exe) page.


## Basic Usage

This simple example is a python adaptation of the [**C#** example of the LibreHardwareMonitor repository](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor#whats-the-easiest-way-to-start).

```python
from HardwareMonitor.Hardware import *  # equivalent to 'using LibreHardwareMonitor.Hardware;'

class UpdateVisitor(IVisitor):
    __namespace__ = "TestHardwareMonitor"  # must be unique among implementations of the IVisitor interface
    def VisitComputer(self, computer: IComputer):
        computer.Traverse(self);

    def VisitHardware(self, hardware: IHardware):
        hardware.Update()
        for subHardware in hardware.SubHardware:
            subHardware.Update()

    def VisitParameter(self, parameter: IParameter): pass

    def VisitSensor(self, sensor: ISensor): pass


computer = Computer()  # settings can not be passed as constructor argument (following below)
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
            print(f"\t\tSensor: {sensor.Name}, value: {sensor.Value}")
    for sensor in hardware.Sensors:
        print(f"\tSensor: {sensor.Name}, value: {sensor.Value}")

computer.Close()
```

---

## Utilities

Utilities are located in the `HardwareMonitor.Util` module.

### Function `OpenComputer`

The `OpenComputer` function provides a shorthand for creating the `HardwareMonitor.Hardware.Computer` instance including the settings and update visitor.  
Settings are given as keyword arguments, the following example enables just the `cpu` and `motherboard` component.

```python
computer = OpenComputer(cpu=True, motherboard=True)  # use 'all=True' to enable every component
# Access sensors
...
computer.Update()  # Updates all sensors
...
computer.Close()
```

### Function `ToBuiltinTypes`

Instances from the `HardwareMonitor` module can be reduced to primitive python types instead of `HardwareMonitor` object instances with the `ToBuiltinTypes` function.  
Objects are recursively converted to Python builtin types (`dict`, `list`, ...).
This can be useful for applications that serialized the data (e.g. with json).

```python
computer = OpenComputer(cpu=True)

data = ToBuiltinTypes(computer.Hardware)
# [{'Type': 'Hardware', 'HardwareType': 'Cpu', 'Name': 'Intel Core i5-8265U', 'Sensors': [...], 'SubHardware': [...]}]
```

### Function `GroupSensorsByType`

Sensors of an instance of `HardwareMonitor.Harware.Hardware` are held in a flat list.  
The helper function `GroupSensorsByType` converts the sensor list into a list of lists grouping sensors by type.

```python
GroupSensorsByType(sensors: Iterable[ISensor]) -> List[List[ISensor]]
```

### Function `SensorValueToString`

The helper function `SensorValueToString` converts sensor values to strings appending with the appropriate unit.

```python
SensorValueToString(value: float, type: SensorType) -> str
# returns "3100.0 MHz" for value=3100.0 with type=SensorType.Clock
```

### Dictionary `HardwareTypeString` and `SensorTypeString`

These two mappings convert values for `HardwareType` (or `SensorType`) to a string.  
Both the integer value for the enum or the instances of the enum value (e.g. `HardwareType.Cpu`) are present as keys.

> In some environments the type fields were set to integers in others to the corresponding type instance.
