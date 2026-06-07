# PyHardwareMonitor Build Instructions

The module is for the most part generated using scripts in the `script` subfolder.

## Build Dependencies/Tools

### dotnet CLI
The [.NET SDK](https://dotnet.microsoft.com/download) (8+) is required to build `LibreHardwareMonitorLib`.
On Windows, the .NET Framework 4.7.2 targeting pack must also be installed (included with Visual Studio or available as a standalone installer).

### MSBuild (Visual Studio / Build Tools)

Required only when rebuilding PyStubbler from source (i.e. after updating the `pythonstubs` submodule).
If the `PyStubbler.exe` binary already exists at `submodules/pythonstubs/builder/bin/PyStubbler.exe`, this step is skipped automatically.

Load the [VisualStudio project](submodules/pythonstubs/builder/PyStubblerNET.sln) file located at `submodules/pythonstubs/builder`.
Build the `PyStubblerNET` solution for `Release` configuration and `x64` target.


## Generate Package files

All steps — including compiling the .NET projects — can be run in one command:

```sh
py scripts/generate_all.py
```

This script performs the following actions

- Build PyStubbler (skipped if already compiled)
- Build `LibreHardwareMonitorLib` for `x64`, `x86`, and `ARM64`
- Copy the resulting DLLs into `HardwareMonitor/lib/{platform}/`
- Regenerate all `.pyi` stub files
- Regenerate all namespace `__init__.py` files

> Note: It is assumed that Python is installed on Windows with the pylauncher option set, and that `dotnet` is available on PATH.
