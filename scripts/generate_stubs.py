import glob
import shutil
import subprocess as sp
from pathlib import Path

BASE_PATH       = Path(__file__).parent.absolute()
MODULE_PATH     = BASE_PATH / ".." / "HardwareMonitor"
MODULE_LIB_PATH = MODULE_PATH / "lib"
SUBMODULE_PATH  = BASE_PATH / ".." / "submodules"

STUBBLER_PATH   = SUBMODULE_PATH / "pythonstubs" / "builder" / "bin" / "PyStubbler.exe"
ASSEMBLY_PATH   = SUBMODULE_PATH / "LibreHardwareMonitor" / "bin" / "Release" / "net4*"

ASSEMBLY_NAMES  = ("LibreHardwareMonitorLib.dll", "HidSharp.dll", "RAMSPDToolkit-NDD.dll")


def collectAssembly():
    for assembly_name in ASSEMBLY_NAMES:
        for lib in map(Path, glob.glob(str(ASSEMBLY_PATH / assembly_name))):
            shutil.copyfile(lib, MODULE_LIB_PATH / lib.name)

def removeExistingStubs():
    for stub in MODULE_PATH.rglob("__init__.pyi"):
        stub.unlink()

def generateStubs():
    assembly_path = list(MODULE_LIB_PATH.glob("*HardwareMonitorLib.dll"))[0]
    return sp.call([str(STUBBLER_PATH), "--dest-is-root", "--dest", str(MODULE_PATH), str(assembly_path)])


if __name__ == "__main__":
    collectAssembly()
    removeExistingStubs()
    generateStubs()
