
import sys
import clr
import ctypes
import logging
from   pathlib import Path


logger = logging.getLogger("PyHardwareMonitor")


def _checkForPawnIO():
    """
    Detect if the PawnIO module is installed by searching for uninstall entry in the registry.
    """
    import winreg
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\PawnIO"
    try:
        access_flags = winreg.KEY_READ
        if sys.maxsize < 2**32:
            access_flags |= winreg.KEY_WOW64_64KEY
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, access_flags):
            return True
    except:
        pass
    return False


if not ctypes.windll.shell32.IsUserAnAdmin():
    logger.warning("Admin privileges are required for 'HardwareMonitor' to work properly.")

if not _checkForPawnIO():
    logger.warning("""PawnIO is not installed - Many sensor will not be available.
    Please install manually through one of the following methods:
        1) Run the terminal command 'winget install PawnIO'
        2) Download and run 'https://github.com/namazso/PawnIO.Setup/releases/latest/download/PawnIO_setup.exe'
""")


ASSEMBLY_NAME = "LibreHardwareMonitor"

_LIB_PATH = Path(__file__).parent.joinpath("lib").absolute()
sys.path.insert(0, str(_LIB_PATH))
__reference__ = clr.AddReference(str(_LIB_PATH / (ASSEMBLY_NAME + "Lib.dll")))

__import__(ASSEMBLY_NAME)
