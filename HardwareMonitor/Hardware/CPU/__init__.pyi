from HardwareMonitor.Hardware import GroupAffinity, Hardware, ISettings
from HardwareMonitor._util.types import UInt32
from typing import List, Set


class CpuId:
    @property
    def Affinity(self) -> GroupAffinity: ...
    @property
    def ApicId(self) -> UInt32: ...
    @property
    def BrandString(self) -> str: ...
    @property
    def CoreId(self) -> UInt32: ...
    @property
    def Data(self) -> List[UInt32]: ...
    @property
    def ExtData(self) -> List[UInt32]: ...
    @property
    def Family(self) -> UInt32: ...
    @property
    def Group(self) -> int: ...
    @property
    def Model(self) -> UInt32: ...
    @property
    def Name(self) -> str: ...
    @property
    def PkgType(self) -> UInt32: ...
    @property
    def ProcessorId(self) -> UInt32: ...
    def Get(group: int, thread: int) -> CpuId: ...
    @property
    def Stepping(self) -> UInt32: ...
    @property
    def Thread(self) -> int: ...
    @property
    def ThreadId(self) -> UInt32: ...
    @property
    def Vendor(self) -> Vendor: ...


class GenericCpu(Hardware):
    def __init__(self, processorIndex: int, cpuId: Set[Set[CpuId]], settings: ISettings): ...
    @property
    def CpuId(self) -> Set[Set[CpuId]]: ...
    @property
    def HardwareType(self) -> HardwareType: ...
    @property
    def HasModelSpecificRegisters(self) -> bool: ...
    @property
    def HasTimeStampCounter(self) -> bool: ...
    @property
    def Index(self) -> int: ...
    @property
    def TimeStampCounterFrequency(self) -> float: ...
    def GetReport(self) -> str: ...
    def Update(self) -> None: ...


class Vendor:
    Unknown = 0
    Intel = 1
    AMD = 2
