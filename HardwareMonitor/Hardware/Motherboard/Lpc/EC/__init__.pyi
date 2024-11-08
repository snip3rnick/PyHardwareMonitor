from HardwareMonitor.Hardware import Hardware, ISettings, SensorType
from HardwareMonitor._util.types import AsyncCallback, Byte, IAsyncResult, IntPtr, Object, Single, UInt16
from typing import Iterable, Set


class BadConfigurationException:
    def __init__(self, message: str): ...


class BusMutexLockingFailedException:
    def __init__(self): ...


class EmbeddedController(Hardware):
    @property
    def HardwareType(self) -> HardwareType: ...
    def GetReport(self) -> str: ...
    def Update(self) -> None: ...


class EmbeddedControllerReader:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, ecIO: IEmbeddedControllerIO, register: UInt16, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> Single: ...
    def Invoke(self, ecIO: IEmbeddedControllerIO, register: UInt16) -> Single: ...


class EmbeddedControllerSource:
    def __init__(self, name: str, type: SensorType, register: UInt16, size: Byte, factor: Single, blank: int): ...
    @property
    def Blank(self) -> int: ...
    @property
    def Factor(self) -> Single: ...
    @property
    def Name(self) -> str: ...
    @property
    def Reader(self) -> EmbeddedControllerReader: ...
    @property
    def Register(self) -> UInt16: ...
    @property
    def Size(self) -> Byte: ...
    @property
    def Type(self) -> SensorType: ...


class IEmbeddedControllerIO:
    def Read(self, registers: Set[UInt16], data: Set[Byte]) -> None: ...


class IOException:
    def __init__(self, message: str): ...


class MultipleBoardRecordsFoundException:
    def __init__(self, model: str): ...


class WindowsEmbeddedController(EmbeddedController):
    def __init__(self, sources: Iterable[EmbeddedControllerSource], settings: ISettings): ...


class WindowsEmbeddedControllerIO:
    def __init__(self): ...
    def Dispose(self) -> None: ...
    def Read(self, registers: Set[UInt16], data: Set[Byte]) -> None: ...
