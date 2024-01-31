from typing import overload, Tuple, Set, Iterable, List
from HardwareMonitor.Hardware import Hardware


class GenericGpu(Hardware):
    @property
    def DeviceId(self) -> str: ...
