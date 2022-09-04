# PyHardwareMonitor

Python Harware Monitor is a thin package layer for [`LibreHardwareMonitorLib`](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor) using [`pythonnet`](https://github.com/pythonnet/pythonnet). 
Libre Hardware Monitor, a fork of Open Hardware Monitor, is free software that can monitor the temperature sensors, fan speeds, voltages, load and clock speeds of your computer. 
This package is mostly auto generated using the [`pythonstubs`](https://github.com/mcneel/pythonstubs) generator tool for .NET libraries.
Scripts for generating, altering and extending package resources are located in the [scripts folder](https://github.com/snip3rnick/PyHardwareMonitor/tree/main/scripts).

The purpose of this layer is the ability to provide extensive typing information and additional utilities around the LibreHardwareMonitorLib.


## Prerequisites
- Python 3.6+
  - pythonnet
  - .NET 4.7


## Installation
```
git clone https://github.com/snip3rnick/PyHardwareMonitor
cd PyHardwareMonitor
pip3 install .
```


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


## Utilities

Utilities are located in the `HardwareMonitor.Util` module.
The `OpenComputer` function provides a shorthand for creating the `HardwareMonitor.Hardware.Computer` instance including the settings and update visitor.  
Settings are given as keyword arguments, the following example just enables the `cpu` and `motherboard` component.

```python
from HardwareMonitor.Util import OpenComputer

computer = OpenComputer(cpu=True, motherboard=True)  # use with 'all=True' to enable every component
...
computer.Close()
```

---

Instances from the `HardwareMonitor` module can be reduced to primitive python types instead of object using the `ToBuiltinTypes` function.  
Objects are recursively converted to Python builtin types (`dict`, `list`, ...) which is particularly useful if the data is to be serialized (e.g. with json).

```python
computer = OpenComputer(motherboard=True)  # use with 'all=True' to enable every component

data = ToBuiltinTypes(computer.Hardware)
# [{'Type': 'Hardware', 'HardwareType': 'Cpu', 'Name': 'Intel Core i5-8265U', 'Sensors': [...], 'SubHardware': [...]}]
```
