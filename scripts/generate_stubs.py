import shutil
import subprocess as sp
from pathlib import Path

BASE_PATH       = Path(__file__).parent.absolute()
MODULE_PATH     = BASE_PATH / ".." / "HardwareMonitor"
MODULE_LIB_PATH = MODULE_PATH / "lib"
SUBMODULE_PATH  = BASE_PATH / ".." / "submodules"

STUBBLER_PATH     = SUBMODULE_PATH / "pythonstubs" / "builder" / "bin" / "PyStubbler.exe"
ASSEMBLY_PATH     = SUBMODULE_PATH / "LibreHardwareMonitor" / "bin" / "Release"
LICENSE_PATH      = SUBMODULE_PATH / "LibreHardwareMonitor" / "LICENSE"
ASSEMBLY_PLATFORMS = ("x64", "x86", "ARM64")

LHM_CSPROJ   = SUBMODULE_PATH / "LibreHardwareMonitor" / "LibreHardwareMonitorLib" / "LibreHardwareMonitorLib.csproj"
STUBBLER_SLN = SUBMODULE_PATH / "pythonstubs" / "builder" / "PyStubblerNET.sln"


def buildLibreHardwareMonitor():
    for platform in ASSEMBLY_PLATFORMS:
        print(f"Building LibreHardwareMonitorLib for {platform}...")
        sp.check_call(["dotnet", "build", str(LHM_CSPROJ),
                       "-c", "Release", f"-p:Platform={platform}",
                       "--nologo", "-v", "m"])

def buildPyStubbler():
    if STUBBLER_PATH.exists():
        print("PyStubbler already built, skipping.")
        return
    print("Building PyStubbler...")
    sp.check_call(["msbuild", str(STUBBLER_SLN),
                   "/p:Configuration=Release", "/p:Platform=x64",
                   "/nologo", "/v:m"])

def collectAssembly():
    for platform in ASSEMBLY_PLATFORMS:
        src = next(iter(sorted((ASSEMBLY_PATH / platform).glob("net4*"))), None)
        if src is None:
            print(f"WARNING: no net4* build found for {platform}, skipping")
            continue
        dest = MODULE_LIB_PATH / platform
        dest.mkdir(exist_ok=True)
        for dll in src.glob("*.dll"):
            shutil.copyfile(dll, dest / dll.name)
    shutil.copyfile(LICENSE_PATH, MODULE_LIB_PATH / LICENSE_PATH.name)

def removeExistingStubs():
    for stub in MODULE_PATH.rglob("__init__.pyi"):
        stub.unlink()

def generateStubs():
    assembly_path = list((MODULE_LIB_PATH / "x64").glob("*HardwareMonitorLib.dll"))[0]
    return sp.call([str(STUBBLER_PATH), "--dest-is-root", "--dest", str(MODULE_PATH), str(assembly_path)])


if __name__ == "__main__":
    collectAssembly()
    removeExistingStubs()
    generateStubs()
