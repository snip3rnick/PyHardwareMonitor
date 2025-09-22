from HardwareMonitor._util.types import AsyncCallback, Byte, DateTime, IAsyncResult, IDictionary, IReadOnlyList, IntPtr, Nullable, Object, Single, TimeSpan, UInt16, UInt32, UInt64
__all__ = ['Cpu','Gpu','Motherboard','Storage']
from typing import Iterable, List, Set, overload


class BaseBoardInformation(InformationBase):
    @property
    def ManufacturerName(self) -> str: ...
    @property
    def ProductName(self) -> str: ...
    @property
    def SerialNumber(self) -> str: ...
    @property
    def Version(self) -> str: ...


class BiosInformation(InformationBase):
    @property
    def Date(self) -> Nullable: ...
    @property
    def Size(self) -> Nullable: ...
    @property
    def Vendor(self) -> str: ...
    @property
    def Version(self) -> str: ...


class CacheAssociativity:
    Other = 1
    Unknown = 2
    DirectMapped = 3
    _2Way = 4
    _4Way = 5
    FullyAssociative = 6
    _8Way = 7
    _16Way = 8
    _12Way = 9
    _24Way = 10
    _32Way = 11
    _48Way = 12
    _64Way = 13
    _20Way = 14


class CacheDesignation:
    Other = 0
    L1 = 1
    L2 = 2
    L3 = 3


class CacheInformation(InformationBase):
    @property
    def Associativity(self) -> CacheAssociativity: ...
    @property
    def Designation(self) -> CacheDesignation: ...
    @property
    def Handle(self) -> UInt16: ...
    @property
    def Size(self) -> UInt16: ...


class Computer:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, settings: ISettings): ...
    def Accept(self, visitor: IVisitor) -> None: ...
    def add_HardwareAdded(self, value: HardwareEventHandler) -> None: ...
    def add_HardwareRemoved(self, value: HardwareEventHandler) -> None: ...
    def Close(self) -> None: ...
    @property
    def Hardware(self) -> List[IHardware]: ...
    @property
    def IsBatteryEnabled(self) -> bool: ...
    @property
    def IsControllerEnabled(self) -> bool: ...
    @property
    def IsCpuEnabled(self) -> bool: ...
    @property
    def IsGpuEnabled(self) -> bool: ...
    @property
    def IsMemoryEnabled(self) -> bool: ...
    @property
    def IsMotherboardEnabled(self) -> bool: ...
    @property
    def IsNetworkEnabled(self) -> bool: ...
    @property
    def IsPsuEnabled(self) -> bool: ...
    @property
    def IsStorageEnabled(self) -> bool: ...
    @property
    def SMBios(self) -> SMBios: ...
    def GetReport(self) -> str: ...
    def Open(self) -> None: ...
    def remove_HardwareAdded(self, value: HardwareEventHandler) -> None: ...
    def remove_HardwareRemoved(self, value: HardwareEventHandler) -> None: ...
    def Reset(self) -> None: ...
    @IsBatteryEnabled.setter
    def IsBatteryEnabled(self, value: bool) -> None: ...
    @IsControllerEnabled.setter
    def IsControllerEnabled(self, value: bool) -> None: ...
    @IsCpuEnabled.setter
    def IsCpuEnabled(self, value: bool) -> None: ...
    @IsGpuEnabled.setter
    def IsGpuEnabled(self, value: bool) -> None: ...
    @IsMemoryEnabled.setter
    def IsMemoryEnabled(self, value: bool) -> None: ...
    @IsMotherboardEnabled.setter
    def IsMotherboardEnabled(self, value: bool) -> None: ...
    @IsNetworkEnabled.setter
    def IsNetworkEnabled(self, value: bool) -> None: ...
    @IsPsuEnabled.setter
    def IsPsuEnabled(self, value: bool) -> None: ...
    @IsStorageEnabled.setter
    def IsStorageEnabled(self, value: bool) -> None: ...
    def Traverse(self, visitor: IVisitor) -> None: ...


class ControlMode:
    Undefined = 0
    Software = 1
    Default = 2


class GroupAffinity:
    def __init__(self, group: UInt16, mask: UInt64): ...
    def Equals(self, o: Object) -> bool: ...
    @property
    def Group(self) -> UInt16: ...
    @property
    def Mask(self) -> UInt64: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(a1: GroupAffinity, a2: GroupAffinity) -> bool: ...
    def op_Inequality(a1: GroupAffinity, a2: GroupAffinity) -> bool: ...
    def Single(group: UInt16, index: int) -> GroupAffinity: ...


class Hardware:
    def Accept(self, visitor: IVisitor) -> None: ...
    def add_Closing(self, value: HardwareEventHandler) -> None: ...
    def add_SensorAdded(self, value: SensorEventHandler) -> None: ...
    def add_SensorRemoved(self, value: SensorEventHandler) -> None: ...
    def Close(self) -> None: ...
    @property
    def HardwareType(self) -> HardwareType: ...
    @property
    def Identifier(self) -> Identifier: ...
    @property
    def Name(self) -> str: ...
    @property
    def Parent(self) -> IHardware: ...
    @property
    def Properties(self) -> IDictionary: ...
    @property
    def Sensors(self) -> Set[ISensor]: ...
    @property
    def SubHardware(self) -> Set[IHardware]: ...
    def GetReport(self) -> str: ...
    def remove_Closing(self, value: HardwareEventHandler) -> None: ...
    def remove_SensorAdded(self, value: SensorEventHandler) -> None: ...
    def remove_SensorRemoved(self, value: SensorEventHandler) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    def Traverse(self, visitor: IVisitor) -> None: ...
    def Update(self) -> None: ...


class HardwareEventHandler:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, hardware: IHardware, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, hardware: IHardware) -> None: ...


class HardwareType:
    Motherboard = 0
    SuperIO = 1
    Cpu = 2
    Memory = 3
    GpuNvidia = 4
    GpuAmd = 5
    GpuIntel = 6
    Storage = 7
    Network = 8
    Cooler = 9
    EmbeddedController = 10
    Psu = 11
    Battery = 12


class IComputer:
    def add_HardwareAdded(self, value: HardwareEventHandler) -> None: ...
    def add_HardwareRemoved(self, value: HardwareEventHandler) -> None: ...
    @property
    def Hardware(self) -> List[IHardware]: ...
    @property
    def IsBatteryEnabled(self) -> bool: ...
    @property
    def IsControllerEnabled(self) -> bool: ...
    @property
    def IsCpuEnabled(self) -> bool: ...
    @property
    def IsGpuEnabled(self) -> bool: ...
    @property
    def IsMemoryEnabled(self) -> bool: ...
    @property
    def IsMotherboardEnabled(self) -> bool: ...
    @property
    def IsNetworkEnabled(self) -> bool: ...
    @property
    def IsPsuEnabled(self) -> bool: ...
    @property
    def IsStorageEnabled(self) -> bool: ...
    def GetReport(self) -> str: ...
    def remove_HardwareAdded(self, value: HardwareEventHandler) -> None: ...
    def remove_HardwareRemoved(self, value: HardwareEventHandler) -> None: ...


class IControl:
    @property
    def ControlMode(self) -> ControlMode: ...
    @property
    def Identifier(self) -> Identifier: ...
    @property
    def MaxSoftwareValue(self) -> Single: ...
    @property
    def MinSoftwareValue(self) -> Single: ...
    @property
    def Sensor(self) -> ISensor: ...
    @property
    def SoftwareValue(self) -> Single: ...
    def SetDefault(self) -> None: ...
    def SetSoftware(self, value: Single) -> None: ...


class ICriticalSensorLimits:
    @property
    def CriticalHighLimit(self) -> Nullable: ...
    @property
    def CriticalLowLimit(self) -> Nullable: ...


class Identifier:
    @overload
    def __init__(self, identifiers: Set[str]): ...
    @overload
    def __init__(self, dev: HidDevice): ...
    @overload
    def __init__(self, identifier: Identifier, extensions: Set[str]): ...
    def CompareTo(self, other: Identifier) -> int: ...
    def Equals(self, obj: Object) -> bool: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(id1: Identifier, id2: Identifier) -> bool: ...
    def op_GreaterThan(id1: Identifier, id2: Identifier) -> bool: ...
    def op_Inequality(id1: Identifier, id2: Identifier) -> bool: ...
    def op_LessThan(id1: Identifier, id2: Identifier) -> bool: ...
    def ToString(self) -> str: ...


class IElement:
    def Accept(self, visitor: IVisitor) -> None: ...
    def Traverse(self, visitor: IVisitor) -> None: ...


class IHardware:
    def add_SensorAdded(self, value: SensorEventHandler) -> None: ...
    def add_SensorRemoved(self, value: SensorEventHandler) -> None: ...
    @property
    def HardwareType(self) -> HardwareType: ...
    @property
    def Identifier(self) -> Identifier: ...
    @property
    def Name(self) -> str: ...
    @property
    def Parent(self) -> IHardware: ...
    @property
    def Properties(self) -> IDictionary: ...
    @property
    def Sensors(self) -> Set[ISensor]: ...
    @property
    def SubHardware(self) -> Set[IHardware]: ...
    def GetReport(self) -> str: ...
    def remove_SensorAdded(self, value: SensorEventHandler) -> None: ...
    def remove_SensorRemoved(self, value: SensorEventHandler) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    def Update(self) -> None: ...


class InformationBase:
    pass


class IParameter:
    @property
    def DefaultValue(self) -> Single: ...
    @property
    def Description(self) -> str: ...
    @property
    def Identifier(self) -> Identifier: ...
    @property
    def IsDefault(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Sensor(self) -> ISensor: ...
    @property
    def Value(self) -> Single: ...
    @IsDefault.setter
    def IsDefault(self, value: bool) -> None: ...
    @Value.setter
    def Value(self, value: Single) -> None: ...


class ISensor:
    def ClearValues(self) -> None: ...
    @property
    def Control(self) -> IControl: ...
    @property
    def Hardware(self) -> IHardware: ...
    @property
    def Identifier(self) -> Identifier: ...
    @property
    def Index(self) -> int: ...
    @property
    def IsDefaultHidden(self) -> bool: ...
    @property
    def Max(self) -> Nullable: ...
    @property
    def Min(self) -> Nullable: ...
    @property
    def Name(self) -> str: ...
    @property
    def Parameters(self) -> IReadOnlyList: ...
    @property
    def SensorType(self) -> SensorType: ...
    @property
    def Value(self) -> Nullable: ...
    @property
    def Values(self) -> Iterable[SensorValue]: ...
    @property
    def ValuesTimeWindow(self) -> TimeSpan: ...
    def ResetMax(self) -> None: ...
    def ResetMin(self) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @ValuesTimeWindow.setter
    def ValuesTimeWindow(self, value: TimeSpan) -> None: ...


class ISensorLimits:
    @property
    def HighLimit(self) -> Nullable: ...
    @property
    def LowLimit(self) -> Nullable: ...


class ISettings:
    def Contains(self, name: str) -> bool: ...
    def GetValue(self, name: str, value: str) -> str: ...
    def Remove(self, name: str) -> None: ...
    def SetValue(self, name: str, value: str) -> None: ...


class IVisitor:
    def VisitComputer(self, computer: IComputer) -> None: ...
    def VisitHardware(self, hardware: IHardware) -> None: ...
    def VisitParameter(self, parameter: IParameter) -> None: ...
    def VisitSensor(self, sensor: ISensor) -> None: ...


class MemoryDevice(InformationBase):
    @property
    def BankLocator(self) -> str: ...
    @property
    def ConfiguredSpeed(self) -> UInt16: ...
    @property
    def ConfiguredVoltage(self) -> UInt16: ...
    @property
    def DeviceLocator(self) -> str: ...
    @property
    def ManufacturerName(self) -> str: ...
    @property
    def PartNumber(self) -> str: ...
    @property
    def SerialNumber(self) -> str: ...
    @property
    def Size(self) -> UInt32: ...
    @property
    def Speed(self) -> UInt16: ...
    @property
    def Type(self) -> MemoryType: ...


class MemoryType:
    Other = 1
    Unknown = 2
    DRAM = 3
    EDRAM = 4
    VRAM = 5
    SRAM = 6
    RAM = 7
    ROM = 8
    FLASH = 9
    EEPROM = 10
    FEPROM = 11
    EPROM = 12
    CDRAM = 13
    _3DRAM = 14
    SDRAM = 15
    SGRAM = 16
    RDRAM = 17
    DDR = 18
    DDR2 = 19
    DDR2_FBDIMM = 20
    DDR3 = 24
    FBD2 = 25
    DDR4 = 26
    LPDDR = 27
    LPDDR2 = 28
    LPDDR3 = 29
    LPDDR4 = 30
    LogicalNonVolatileDevice = 31
    HBM = 32
    HBM2 = 33
    DDR5 = 34
    LPDDR5 = 35


class ParameterDescription:
    def __init__(self, name: str, description: str, defaultValue: Single): ...
    @property
    def DefaultValue(self) -> Single: ...
    @property
    def Description(self) -> str: ...
    @property
    def Name(self) -> str: ...


class ProcessorCharacteristics:
    #None = 0
    _64BitCapable = 1
    MultiCore = 2
    HardwareThread = 4
    ExecuteProtection = 8
    EnhancedVirtualization = 16
    PowerPerformanceControl = 32
    _128BitCapable = 64


class ProcessorFamily:
    Other = 1
    Intel8086 = 3
    Intel80286 = 4
    Intel386 = 5
    Intel486 = 6
    Intel8087 = 7
    Intel80287 = 8
    Intel80387 = 9
    Intel80487 = 10
    IntelPentium = 11
    IntelPentiumPro = 12
    IntelPentiumII = 13
    IntelPentiumMMX = 14
    IntelCeleron = 15
    IntelPentiumIIXeon = 16
    IntelPentiumIII = 17
    M1 = 18
    M2 = 19
    IntelCeleronM = 20
    IntelPentium4HT = 21
    AmdDuron = 24
    AmdK5 = 25
    AmdK6 = 26
    AmdK62 = 27
    AmdK63 = 28
    AmdAthlon = 29
    Amd2900 = 30
    AmdK62Plus = 31
    PowerPc = 32
    PowerPc601 = 33
    PowerPc603 = 34
    PowerPc603Plus = 35
    PowerPc604 = 36
    PowerPc620 = 37
    PowerPcx704 = 38
    PowerPc750 = 39
    IntelCoreDuo = 40
    IntelCoreDuoMobile = 41
    IntelCoreSoloMobile = 42
    IntelAtom = 43
    IntelCoreM = 44
    IntelCoreM3 = 45
    IntelCoreM5 = 46
    IntelCoreM7 = 47
    Alpha = 48
    Alpha21064 = 49
    Alpha21066 = 50
    Alpha21164 = 51
    Alpha21164Pc = 52
    Alpha21164a = 53
    Alpha21264 = 54
    Alpha21364 = 55
    AmdTurionIIUltraDualCoreMobileM = 56
    AmdTurionDualCoreMobileM = 57
    AmdAthlonIIDualCoreM = 58
    AmdOpteron6100Series = 59
    AmdOpteron4100Series = 60
    AmdOpteron6200Series = 61
    AmdOpteron4200Series = 62
    AmdFxSeries = 63
    Mips = 64
    MipsR4000 = 65
    MipsR4200 = 66
    MipsR4400 = 67
    MipsR4600 = 68
    MipsR10000 = 69
    AmdCSeries = 70
    AmdESeries = 71
    AmdASeries = 72
    AmdGSeries = 73
    AmdZSeries = 74
    AmdRSeries = 75
    AmdOpteron4300Series = 76
    AmdOpteron6300Series = 77
    AmdOpteron3300Series = 78
    AmdFireProSeries = 79
    Sparc = 80
    SuperSparc = 81
    MicroSparcII = 82
    MicroSparcIIep = 83
    UltraSparc = 84
    UltraSparcII = 85
    UltraSparcIIi = 86
    UltraSparcIII = 87
    UltraSparcIIIi = 88
    Motorola68040 = 96
    Motorola68xxx = 97
    Motorola68000 = 98
    Motorola68010 = 99
    Motorola68020 = 100
    Motorola68030 = 101
    AmdAthlonX4QuadCore = 102
    AmdOpteronX1000Series = 103
    AmdOpteronX2000Series = 104
    AmdOpteronASeries = 105
    AmdOpteronX3000Series = 106
    AmdZen = 107
    Hobbit = 112
    CrusoeTm5000 = 120
    CrusoeTm3000 = 121
    EfficeonTm8000 = 122
    Weitek = 128
    IntelItanium = 130
    AmdAthlon64 = 131
    AmdOpteron = 132
    AmdSempron = 133
    AmdTurio64Mobile = 134
    AmdOpteronDualCore = 135
    AmdAthlon64X2DualCore = 136
    AmdTurion64X2Mobile = 137
    AmdOpteronQuadCore = 138
    AmdOpteronThirdGen = 139
    AmdPhenomFXQuadCore = 140
    AmdPhenomX4QuadCore = 141
    AmdPhenomX2DualCore = 142
    AmdAthlonX2DualCore = 143
    PaRisc = 144
    PaRisc8500 = 145
    PaRisc8000 = 146
    PaRisc7300LC = 147
    PaRisc7200 = 148
    PaRisc7100LC = 149
    PaRisc7100 = 150
    V30 = 160
    IntelXeon3200QuadCoreSeries = 161
    IntelXeon3000DualCoreSeries = 162
    IntelXeon5300QuadCoreSeries = 163
    IntelXeon5100DualCoreSeries = 164
    IntelXeon5000DualCoreSeries = 165
    IntelXeonLVDualCore = 166
    IntelXeonULVDualCore = 167
    IntelXeon7100Series = 168
    IntelXeon5400Series = 169
    IntelXeonQuadCore = 170
    IntelXeon5200DualCoreSeries = 171
    IntelXeon7200DualCoreSeries = 172
    IntelXeon7300QuadCoreSeries = 173
    IntelXeon7400QuadCoreSeries = 174
    IntelXeon7400MultiCoreSeries = 175
    IntelPentiumIIIXeon = 176
    IntelPentiumIIISpeedStep = 177
    IntelPentium4 = 178
    IntelXeon = 179
    As400 = 180
    IntelXeonMP = 181
    AmdAthlonXP = 182
    AmdAthlonMP = 183
    IntelItanium2 = 184
    IntelPentiumM = 185
    IntelCeleronD = 186
    IntelPentiumD = 187
    IntelPentiumExtreme = 188
    IntelCoreSolo = 189
    IntelCore2Duo = 191
    IntelCore2Solo = 192
    IntelCore2Extreme = 193
    IntelCore2Quad = 194
    IntelCore2ExtremeMobile = 195
    IntelCore2DuoMobile = 196
    IntelCore2SoloMobile = 197
    IntelCoreI7 = 198
    IntelCeleronDualCore = 199
    Ibm390 = 200
    PowerPcG4 = 201
    PowerPcG5 = 202
    Esa390G6 = 203
    ZArchitecture = 204
    IntelCoreI5 = 205
    IntelCoreI3 = 206
    IntelCoreI9 = 207
    ViaC7M = 210
    ViaC7D = 211
    ViaC7 = 212
    ViaEden = 213
    IntelXeonMultiCore = 214
    IntelXeon3xxxDualCoreSeries = 215
    IntelXeon3xxxQuadCoreSeries = 216
    ViaNano = 217
    IntelXeon5xxxDualCoreSeries = 218
    IntelXeon5xxxQuadCoreSeries = 219
    IntelXeon7xxxDualCoreSeries = 221
    IntelXeon7xxxQuadCoreSeries = 222
    IntelXeon7xxxMultiCoreSeries = 223
    IntelXeon3400MultiCoreSeries = 224
    AmdOpteron3000Series = 228
    AmdSempronII = 229
    AmdOpteronQuadCoreEmbedded = 230
    AmdPhenomTripleCore = 231
    AmdTurionUltraDualCoreMobile = 232
    AmdTurionDualCoreMobile = 233
    AmdTurionDualCore = 234
    AmdAthlonDualCore = 235
    AmdSempronSI = 236
    AmdPhenomII = 237
    AmdAthlonII = 238
    AmdOpteronSixCore = 239
    AmdSempronM = 240
    IntelI860 = 250
    IntelI960 = 251
    ArmV7 = 256
    ArmV8 = 257
    HitachiSh3 = 258
    HitachiSh4 = 259
    Arm = 260
    StrongArm = 261
    _686 = 262
    MediaGX = 263
    MII = 264
    WinChip = 265
    Dsp = 266
    VideoProcessor = 267


class ProcessorInformation(InformationBase):
    @property
    def Characteristics(self) -> ProcessorCharacteristics: ...
    @property
    def CoreCount(self) -> UInt16: ...
    @property
    def CoreEnabled(self) -> UInt16: ...
    @property
    def CurrentSpeed(self) -> UInt16: ...
    @property
    def ExternalClock(self) -> UInt16: ...
    @property
    def Family(self) -> ProcessorFamily: ...
    @property
    def Handle(self) -> UInt16: ...
    @property
    def Id(self) -> UInt64: ...
    @property
    def L1CacheHandle(self) -> UInt16: ...
    @property
    def L2CacheHandle(self) -> UInt16: ...
    @property
    def L3CacheHandle(self) -> UInt16: ...
    @property
    def ManufacturerName(self) -> str: ...
    @property
    def MaxSpeed(self) -> UInt16: ...
    @property
    def ProcessorType(self) -> ProcessorType: ...
    @property
    def Serial(self) -> str: ...
    @property
    def Socket(self) -> ProcessorSocket: ...
    @property
    def SocketDesignation(self) -> str: ...
    @property
    def ThreadCount(self) -> UInt16: ...
    @property
    def Version(self) -> str: ...


class ProcessorSocket:
    Other = 1
    Unknown = 2
    DaughterBoard = 3
    ZifSocket = 4
    PiggyBack = 5
    #None = 6
    LifSocket = 7
    Zif423 = 13
    A = 14
    Zif478 = 15
    Zif754 = 16
    Zif940 = 17
    Zif939 = 18
    MPga604 = 19
    Lga771 = 20
    Lga775 = 21
    S1 = 22
    AM2 = 23
    F = 24
    Lga1366 = 25
    G34 = 26
    AM3 = 27
    C32 = 28
    Lga1156 = 29
    Lga1567 = 30
    Pga988A = 31
    Bga1288 = 32
    RPga088B = 33
    Bga1023 = 34
    Bga1224 = 35
    Lga1155 = 36
    Lga1356 = 37
    Lga2011 = 38
    FS1 = 39
    FS2 = 40
    FM1 = 41
    FM2 = 42
    Lga20113 = 43
    Lga13563 = 44
    Lga1150 = 45
    Bga1168 = 46
    Bga1234 = 47
    Bga1364 = 48
    AM4 = 49
    Lga1151 = 50
    Bga1356 = 51
    Bga1440 = 52
    Bga1515 = 53
    Lga36471 = 54
    SP3 = 55
    SP3R2 = 56
    Lga2066 = 57
    Bga1510 = 58
    Bga1528 = 59
    Lga4189 = 60


class ProcessorType:
    Other = 1
    Unknown = 2
    CentralProcessor = 3
    MathProcessor = 4
    DspProcessor = 5
    VideoProcessor = 6


class SensorEventHandler:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, sensor: ISensor, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sensor: ISensor) -> None: ...


class SensorType:
    Voltage = 0
    Current = 1
    Power = 2
    Clock = 3
    Temperature = 4
    Load = 5
    Frequency = 6
    Fan = 7
    Flow = 8
    Control = 9
    Level = 10
    Factor = 11
    Data = 12
    SmallData = 13
    Throughput = 14
    TimeSpan = 15
    Timing = 16
    Energy = 17
    Noise = 18
    Conductivity = 19
    Humidity = 20


class SensorValue:
    def __init__(self, value: Single, time: DateTime): ...
    @property
    def Time(self) -> DateTime: ...
    @property
    def Value(self) -> Single: ...


class SensorVisitor:
    def __init__(self, handler: SensorEventHandler): ...
    def VisitComputer(self, computer: IComputer) -> None: ...
    def VisitHardware(self, hardware: IHardware) -> None: ...
    def VisitParameter(self, parameter: IParameter) -> None: ...
    def VisitSensor(self, sensor: ISensor) -> None: ...


class SMBios:
    def __init__(self): ...
    @property
    def Bios(self) -> BiosInformation: ...
    @property
    def Board(self) -> BaseBoardInformation: ...
    @property
    def MemoryDevices(self) -> Set[MemoryDevice]: ...
    @property
    def ProcessorCaches(self) -> Set[CacheInformation]: ...
    @property
    def Processors(self) -> Set[ProcessorInformation]: ...
    @property
    def System(self) -> SystemInformation: ...
    @property
    def SystemEnclosure(self) -> SystemEnclosure: ...
    def GetReport(self) -> str: ...


class SystemEnclosure(InformationBase):
    @property
    def AssetTag(self) -> str: ...
    @property
    def BootUpState(self) -> SystemEnclosureState: ...
    @property
    def LockDetected(self) -> bool: ...
    @property
    def ManufacturerName(self) -> str: ...
    @property
    def PowerCords(self) -> Byte: ...
    @property
    def PowerSupplyState(self) -> SystemEnclosureState: ...
    @property
    def RackHeight(self) -> Byte: ...
    @property
    def SecurityStatus(self) -> SystemEnclosureSecurityStatus: ...
    @property
    def SerialNumber(self) -> str: ...
    @property
    def SKU(self) -> str: ...
    @property
    def ThermalState(self) -> SystemEnclosureState: ...
    @property
    def Type(self) -> SystemEnclosureType: ...
    @property
    def Version(self) -> str: ...
    @LockDetected.setter
    def LockDetected(self, value: bool) -> None: ...
    @SecurityStatus.setter
    def SecurityStatus(self, value: SystemEnclosureSecurityStatus) -> None: ...


class SystemEnclosureSecurityStatus:
    Other = 1
    Unknown = 2
    #None = 3
    ExternalInterfaceLockedOut = 4
    ExternalInterfaceEnabled = 5


class SystemEnclosureState:
    Other = 1
    Unknown = 2
    Safe = 3
    Warning = 4
    Critical = 5
    NonRecoverable = 6


class SystemEnclosureType:
    Other = 1
    Unknown = 2
    Desktop = 3
    LowProfileDesktop = 4
    PizzaBox = 5
    MiniTower = 6
    Tower = 7
    Portable = 8
    Laptop = 9
    Notebook = 10
    HandHeld = 11
    DockingStation = 12
    AllInOne = 13
    SubNotebook = 14
    SpaceSaving = 15
    LunchBox = 16
    MainServerChassis = 17
    ExpansionChassis = 18
    SubChassis = 19
    BusExpansionChassis = 20
    PeripheralChassis = 21
    RaidChassis = 22
    RackMountChassis = 23
    SealedCasePc = 24
    MultiSystemChassis = 25
    CompactPci = 26
    AdvancedTca = 27
    Blade = 28
    BladeEnclosure = 29
    Tablet = 30
    Convertible = 31
    Detachable = 32
    IoTGateway = 33
    EmbeddedPc = 34
    MiniPc = 35
    StickPc = 36


class SystemInformation(InformationBase):
    @property
    def Family(self) -> str: ...
    @property
    def ManufacturerName(self) -> str: ...
    @property
    def ProductName(self) -> str: ...
    @property
    def SerialNumber(self) -> str: ...
    @property
    def Version(self) -> str: ...
    @property
    def WakeUp(self) -> SystemWakeUp: ...


class SystemWakeUp:
    Reserved = 0
    Other = 1
    Unknown = 2
    ApmTimer = 3
    ModemRing = 4
    LanRemote = 5
    PowerSwitch = 6
    PciPme = 7
    AcPowerRestored = 8
