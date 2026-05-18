from HardwareMonitor._util.types import DateTime, UInt16, UInt32
from typing import List, Set, overload


class AVG:
    AVG_22MS = 0
    AVG_44MS = 1
    AVG_89MS = 2
    AVG_177MS = 3
    AVG_354MS = 4
    AVG_709MS = 5
    AVG_1417MS = 6


class CurrentScale:
    CurrentScale5A = 0
    CurrentScale10A = 1
    CurrentScale15A = 2
    CurrentScale20A = 3


class DeviceConfigStructV1:
    pass


class DeviceConfigStructV2:
    pass


class DeviceConfigStructV3:
    pass


class DeviceData:
    def __init__(self): ...
    @property
    def Connected(self) -> bool: ...
    @property
    def ExternalTemp1C(self) -> float: ...
    @property
    def ExternalTemp2C(self) -> float: ...
    @property
    def FaultLog(self) -> UInt16: ...
    @property
    def FaultStatus(self) -> UInt16: ...
    @property
    def FirmwareVersion(self) -> str: ...
    @property
    def HardwareRevision(self) -> str: ...
    @property
    def OnboardTempInC(self) -> float: ...
    @property
    def OnboardTempOutC(self) -> float: ...
    @property
    def PinCurrent(self) -> Set[float]: ...
    @property
    def PinVoltage(self) -> Set[float]: ...
    @property
    def PsuCapabilityW(self) -> int: ...
    @property
    def SumCurrentA(self) -> float: ...
    @property
    def SumPowerW(self) -> float: ...
    @property
    def Timestamp(self) -> DateTime: ...
    @Connected.setter
    def Connected(self, value: bool) -> None: ...
    @ExternalTemp1C.setter
    def ExternalTemp1C(self, value: float) -> None: ...
    @ExternalTemp2C.setter
    def ExternalTemp2C(self, value: float) -> None: ...
    @FaultLog.setter
    def FaultLog(self, value: UInt16) -> None: ...
    @FaultStatus.setter
    def FaultStatus(self, value: UInt16) -> None: ...
    @FirmwareVersion.setter
    def FirmwareVersion(self, value: str) -> None: ...
    @HardwareRevision.setter
    def HardwareRevision(self, value: str) -> None: ...
    @OnboardTempInC.setter
    def OnboardTempInC(self, value: float) -> None: ...
    @OnboardTempOutC.setter
    def OnboardTempOutC(self, value: float) -> None: ...
    @PinCurrent.setter
    def PinCurrent(self, value: Set[float]) -> None: ...
    @PinVoltage.setter
    def PinVoltage(self, value: Set[float]) -> None: ...
    @PsuCapabilityW.setter
    def PsuCapabilityW(self, value: int) -> None: ...
    @Timestamp.setter
    def Timestamp(self, value: DateTime) -> None: ...


class DISPLAY_INVERSION:
    DISPLAY_INVERSION_OFF = 0
    DISPLAY_INVERSION_ON = 1
    DISPLAY_INVERSION_NUM = 2


class DisplayRotation:
    DisplayRotation0 = 0
    DisplayRotation180 = 1


class FanConfigStruct:
    pass


class FanMode:
    FanModeCurve = 0
    FanModeFixed = 1


class HpwrCapability:
    PSU_CAP_600W = 0
    PSU_CAP_450W = 1
    PSU_CAP_300W = 2
    PSU_CAP_150W = 3


class NVM_CMD:
    NVM_CMD_NONE = 0
    NVM_CMD_LOAD = 1
    NVM_CMD_STORE = 2
    NVM_CMD_RESET = 3
    NVM_CMD_LOAD_CAL = 4
    NVM_CMD_STORE_CAL = 5
    NVM_CMD_LOAD_CAL_FACTORY = 6
    NVM_CMD_STORE_CAL_FACTORY = 7


class PowerScale:
    PowerScaleAuto = 0
    PowerScale300W = 1
    PowerScale600W = 2


class PowerSensor:
    pass


class Screen:
    ScreenMain = 0
    ScreenSimple = 1
    ScreenCurrent = 2
    ScreenTemp = 3
    ScreenStatus = 4


class SCREEN_CMD:
    SCREEN_GOTO_MAIN = 224
    SCREEN_GOTO_SIMPLE = 225
    SCREEN_GOTO_CURRENT = 226
    SCREEN_GOTO_TEMP = 227
    SCREEN_GOTO_STATUS = 228
    SCREEN_GOTO_SAME = 239
    SCREEN_PAUSE_UPDATES = 240
    SCREEN_RESUME_UPDATES = 241


class SensorStruct:
    pass


class SensorTs:
    SENSOR_TS_IN = 0
    SENSOR_TS_OUT = 1
    SENSOR_TS3 = 2
    SENSOR_TS4 = 3


class Stm32PortFinder:
    @overload
    def FindMatchingComPorts(vid: UInt32, pid: UInt32) -> List: ...
    @overload
    def FindMatchingComPorts(vid: str, pid: str) -> List: ...


class StructureConversion:
    def ConvertConfigV1ToV2(configV1: DeviceConfigStructV1) -> DeviceConfigStructV2: ...
    def ConvertConfigV1ToV3(configV1: DeviceConfigStructV1) -> DeviceConfigStructV3: ...
    def ConvertConfigV2ToV1(configV2: DeviceConfigStructV2) -> DeviceConfigStructV1: ...
    def ConvertConfigV2ToV3(configV2: DeviceConfigStructV2) -> DeviceConfigStructV3: ...
    def ConvertConfigV3ToV1(configV3: DeviceConfigStructV3) -> DeviceConfigStructV1: ...
    def ConvertConfigV3ToV2(configV3: DeviceConfigStructV3) -> DeviceConfigStructV2: ...


class TempSource:
    TempSourceTsIn = 0
    TempSourceTsOut = 1
    TempSourceTs1 = 2
    TempSourceTs2 = 3
    TempSourceTmax = 4


class Theme:
    ThemeTg1 = 0
    ThemeTg2 = 1
    ThemeTg3 = 2


class THEME_BACKGROUND:
    ThermalGrizzlyOrange = 1
    ThermalGrizzlyDark = 2
    Disabled = 255


class THEME_FAN:
    ThermalGrizzlyOrange = 100
    ThermalGrizzlyDark = 117
    ThermalGrizzlyBlackWhite = 152


class TimeoutMode:
    TimeoutModeStatic = 0
    TimeoutModeCycle = 1
    TimeoutModeSleep = 2


class UiConfigStructV1:
    pass


class UiConfigStructV2:
    pass


class UsbCmd:
    CMD_WELCOME = 0
    CMD_READ_VENDOR_DATA = 1
    CMD_READ_UID = 2
    CMD_READ_DEVICE_DATA = 3
    CMD_READ_SENSOR_VALUES = 4
    CMD_READ_CONFIG = 5
    CMD_WRITE_CONFIG = 6
    CMD_READ_CALIBRATION = 7
    CMD_WRITE_CALIBRATION = 8
    CMD_SPI_FLASH_WRITE_PAGE = 9
    CMD_SPI_FLASH_READ_PAGE = 10
    CMD_SPI_FLASH_ERASE_SECTOR = 11
    CMD_SCREEN_CHANGE = 12
    CMD_READ_BUILD_INFO = 13
    CMD_CLEAR_FAULTS = 14
    CMD_RESET = 240
    CMD_BOOTLOADER = 241
    CMD_NVM_CONFIG = 242
    CMD_NOP = 255


class VendorDataStruct:
    pass
