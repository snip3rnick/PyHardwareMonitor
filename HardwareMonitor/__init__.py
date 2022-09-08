
import sys
import clr
import ctypes
import logging
from   pathlib import Path


logging.basicConfig(format='%(levelname)s: %(message)s')


if not ctypes.windll.shell32.IsUserAnAdmin():
    logging.warning("Admin privileges are required for 'HarwareMonitor' to work properly")

ASSEMBLY_NAME = "LibreHardwareMonitor"

_LIB_PATH = Path(__file__).parent.joinpath("lib").absolute()
sys.path.insert(0, str(_LIB_PATH))
__reference__ = clr.AddReference(str(_LIB_PATH / (ASSEMBLY_NAME + "Lib.dll")))

__import__(ASSEMBLY_NAME)
