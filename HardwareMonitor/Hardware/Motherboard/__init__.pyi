from HardwareMonitor._util.types import IDictionary
from HardwareMonitor.Hardware import IHardware, ISensor, ISettings, IVisitor, SensorEventHandler
from typing import overload, Tuple, Set, Iterable, List


class Manufacturer:
    Abit = 0
    Acer = 1
    Alienware = 2
    AMD = 3
    AOpen = 4
    Apple = 5
    ASRock = 6
    ASUS = 7
    Biostar = 8
    Clevo = 9
    Dell = 10
    DFI = 11
    ECS = 12
    EPoX = 13
    EVGA = 14
    FIC = 15
    Foxconn = 16
    Fujitsu = 17
    Gateway = 18
    Gigabyte = 19
    HP = 20
    IBM = 21
    Intel = 22
    Jetway = 23
    LattePanda = 24
    Lenovo = 25
    Medion = 26
    Microsoft = 27
    MSI = 28
    NEC = 29
    Pegatron = 30
    Samsung = 31
    Sapphire = 32
    Shuttle = 33
    Sony = 34
    Supermicro = 35
    Toshiba = 36
    XFX = 37
    Zotac = 38
    Unknown = 39


class Model:
    _880GMH_USB3 = 0
    A320M_HDV = 1
    AB350_Pro4 = 2
    AB350M = 3
    AB350M_HDV = 4
    AB350M_Pro4 = 5
    AOD790GX_128M = 6
    B450_Pro4 = 7
    B450_Steel_Legend = 8
    B450M_Pro4 = 9
    B450M_Steel_Legend = 10
    B85M_DGS = 11
    Fatal1ty_AB350_Gaming_K4 = 12
    P55_Deluxe = 13
    X399_Phantom_Gaming_6 = 14
    Z77Pro4M = 15
    X570_Pro4 = 16
    X570_Taichi = 17
    X570_Phantom_Gaming_ITX = 18
    Z790_Taichi = 19
    CROSSHAIR_III_FORMULA = 20
    ROG_CROSSHAIR_VIII_HERO = 21
    ROG_CROSSHAIR_VIII_HERO_WIFI = 22
    ROG_CROSSHAIR_VIII_DARK_HERO = 23
    ROG_CROSSHAIR_VIII_FORMULA = 24
    ROG_CROSSHAIR_VIII_IMPACT = 25
    ROG_STRIX_X470_I = 26
    ROG_CROSSHAIR_X670E_EXTREME = 27
    ROG_CROSSHAIR_X670E_HERO = 28
    ROG_CROSSHAIR_X670E_GENE = 29
    ROG_STRIX_X670E_E_GAMING_WIFI = 30
    ROG_STRIX_X670E_F_GAMING_WIFI = 31
    ROG_STRIX_X570_E_GAMING = 32
    ROG_STRIX_X570_F_GAMING = 33
    ROG_STRIX_X570_I_GAMING = 34
    ROG_STRIX_B550_E_GAMING = 35
    ROG_STRIX_B550_F_GAMING_WIFI = 36
    ROG_STRIX_B550_I_GAMING = 37
    ROG_STRIX_Z390_E_GAMING = 38
    ROG_STRIX_Z390_F_GAMING = 39
    ROG_STRIX_Z390_I_GAMING = 40
    ROG_STRIX_Z690_A_GAMING_WIFI_D4 = 41
    ROG_MAXIMUS_XI_FORMULA = 42
    ROG_MAXIMUS_X_HERO_WIFI_AC = 43
    ROG_MAXIMUS_Z690_FORMULA = 44
    ROG_MAXIMUS_Z690_HERO = 45
    ROG_MAXIMUS_Z690_EXTREME_GLACIAL = 46
    ROG_STRIX_Z790_I_GAMING_WIFI = 47
    M2N_SLI_Deluxe = 48
    M4A79XTD_EVO = 49
    P5W_DH_Deluxe = 50
    P6T = 51
    P6X58D_E = 52
    P8P67 = 53
    P8P67_EVO = 54
    P8P67_M_PRO = 55
    P8P67_PRO = 56
    P8Z77_V = 57
    P9X79 = 58
    PRIME_X370_PRO = 59
    PRIME_X470_PRO = 60
    PRIME_X570_PRO = 61
    PROART_X570_CREATOR_WIFI = 62
    PRO_WS_X570_ACE = 63
    RAMPAGE_EXTREME = 64
    RAMPAGE_II_GENE = 65
    ROG_MAXIMUS_X_APEX = 66
    ROG_ZENITH_EXTREME = 67
    ROG_ZENITH_II_EXTREME = 68
    TUF_X470_PLUS_GAMING = 69
    Z170_A = 70
    TUF_GAMING_B550M_PLUS_WIFI = 71
    ROG_MAXIMUS_Z790_HERO = 72
    PRIME_Z690_A = 73
    ROG_MAXIMUS_Z790_FORMULA = 74
    B660GTN = 75
    X670E_Valkyrie = 76
    LP_BI_P45_T2RS_Elite = 77
    LP_DK_P55_T3EH9 = 78
    A890GXM_A = 79
    B350_Gaming_Plus = 80
    B360M_PRO_VDH = 81
    B450A_PRO = 82
    Z270_PC_MATE = 83
    Z77_MS7751 = 84
    Z68_MS7672 = 85
    X570_Gaming_Plus = 86
    X58_SLI_Classified = 87
    X58_3X_SLI = 88
    _965P_S3 = 89
    _970A_UD3 = 90
    AB350_Gaming_3 = 91
    AX370_Gaming_5 = 92
    AX370_Gaming_K7 = 93
    B360_AORUS_GAMING_3_WIFI_CF = 94
    B550_AORUS_PRO = 95
    B560M_AORUS_ELITE = 96
    B560M_AORUS_PRO = 97
    B560M_AORUS_PRO_AX = 98
    B660M_DS3H_AX_DDR4 = 99
    EP45_DS3R = 100
    EP45_UD3R = 101
    EX58_EXTREME = 102
    EX58_UD3R = 103
    G41M_COMBO = 104
    G41MT_S2 = 105
    G41MT_S2P = 106
    H55_USB3 = 107
    H55N_USB3 = 108
    H61M_DS2_REV_1_2 = 109
    H61M_USB3_B3_REV_2_0 = 110
    H67A_UD3H_B3 = 111
    H67A_USB3_B3 = 112
    H81M_HD3 = 113
    B75M_D3H = 114
    MA770T_UD3 = 115
    MA770T_UD3P = 116
    MA785GM_US2H = 117
    MA785GMT_UD2H = 118
    MA78LM_S2H = 119
    MA790X_UD3P = 120
    P35_DS3 = 121
    P35_DS3L = 122
    P55_UD4 = 123
    P55A_UD3 = 124
    P55M_UD4 = 125
    P67A_UD3_B3 = 126
    P67A_UD3R_B3 = 127
    P67A_UD4_B3 = 128
    P8Z68_V_PRO = 129
    X38_DS5 = 130
    X399_AORUS_Gaming_7 = 131
    X58A_UD3R = 132
    X79_UD3 = 133
    Z390_AORUS_ULTRA = 134
    Z390_AORUS_PRO = 135
    Z390_M_GAMING = 136
    Z390_UD = 137
    Z68A_D3H_B3 = 138
    Z68AP_D3 = 139
    Z68X_UD3H_B3 = 140
    Z68X_UD7_B3 = 141
    Z68XP_UD3R = 142
    Z690_AORUS_PRO = 143
    Z690_AORUS_ULTRA = 144
    Z690_GAMING_X_DDR4 = 145
    Z170N_WIFI = 146
    X470_AORUS_GAMING_7_WIFI = 147
    X570_AORUS_MASTER = 148
    X570_GAMING_X = 149
    X570_AORUS_ULTRA = 150
    FH67 = 151
    Unknown = 152


class Motherboard:
    def __init__(self, smBios: SMBios, settings: ISettings): ...
    def Accept(self, visitor: IVisitor) -> None: ...
    def add_SensorAdded(self, value: SensorEventHandler) -> None: ...
    def add_SensorRemoved(self, value: SensorEventHandler) -> None: ...
    def Close(self) -> None: ...
    @property
    def HardwareType(self) -> HardwareType: ...
    @property
    def Identifier(self) -> Identifier: ...
    @property
    def Manufacturer(self) -> Manufacturer: ...
    @property
    def Model(self) -> Model: ...
    @property
    def Name(self) -> str: ...
    @property
    def Parent(self) -> IHardware: ...
    @property
    def Properties(self) -> IDictionary: ...
    @property
    def Sensors(self) -> Set[ISensor]: ...
    @property
    def SMBios(self) -> SMBios: ...
    @property
    def SubHardware(self) -> Set[IHardware]: ...
    def GetReport(self) -> str: ...
    def remove_SensorAdded(self, value: SensorEventHandler) -> None: ...
    def remove_SensorRemoved(self, value: SensorEventHandler) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    def Traverse(self, visitor: IVisitor) -> None: ...
    def Update(self) -> None: ...
