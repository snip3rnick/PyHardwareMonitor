
import sys
import clr
from pathlib import Path


ASSEMBLY_NAME = "LibreHardwareMonitor"

_LIB_PATH = Path(__file__).parent.joinpath("lib").absolute()
sys.path.insert(0, str(_LIB_PATH))
__reference__ = clr.AddReference(str(_LIB_PATH / ("ASSEMBLY_NAME" + "Lib.dll")))

__import__(ASSEMBLY_NAME)
