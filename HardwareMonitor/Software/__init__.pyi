from HardwareMonitor._util.types import OperatingSystem
from typing import overload, Tuple, Set, Iterable, List


class OperatingSystem:
    @property
    def Is64Bit() -> bool: ...
    @property
    def IsUnix() -> bool: ...
    @property
    def IsWindows8OrGreater() -> bool: ...
