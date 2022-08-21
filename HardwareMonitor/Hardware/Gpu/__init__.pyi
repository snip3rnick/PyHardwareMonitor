from typing import overload, Tuple, Set, Iterable, List


class GenericGpu(Hardware):
    @property
    def DeviceId(self) -> str: ...
