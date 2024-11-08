# PyHardwareMonitor Build Instructions

The module is for the most part generated using scripts in the `script` subfolder.

## Build Dependencies/Tools

### LibreHardwareMonitorLib
Load the [submodules/LibreHardwareMonitor/LibreHardwareMonitor.sln](VisualStudio project) file located at `submodules/LibreHardwareMonitor`.
Build the `LibreHardwareMonitorLib` solution for `Release` configuration and `Any CPU` target.

### PyStubbler
Load the [submodules/pythonstubs/builder/PyStubblerNET.sln](VisualStudio project) file located at `submodules/pythonstubs/builder`.
Build the `PyStubblerNET` solution for `Release` configuration and `Any CPU` target.


## Generate Package files

All the module generator steps can be run in one command

```sh
py scripts/generate_all.py
```
> Note: It is assumed that python is installed on Windows with the pylauncher option set.
