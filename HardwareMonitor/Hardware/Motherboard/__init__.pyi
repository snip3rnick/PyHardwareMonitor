from HardwareMonitor.Hardware import IHardware, ISensor, ISettings, IVisitor, SensorEventHandler
from HardwareMonitor._util.types import IDictionary
from typing import Set


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
    ROG_STRIX_X670E_F_GAMING_WIFI = 30
    ROG_STRIX_X570_E_GAMING = 31
    ROG_STRIX_X570_F_GAMING = 32
    ROG_STRIX_X570_I_GAMING = 33
    ROG_STRIX_B550_E_GAMING = 34
    ROG_STRIX_B550_F_GAMING_WIFI = 35
    ROG_STRIX_B550_I_GAMING = 36
    ROG_STRIX_Z390_E_GAMING = 37
    ROG_STRIX_Z390_F_GAMING = 38
    ROG_STRIX_Z390_I_GAMING = 39
    ROG_STRIX_Z690_A_GAMING_WIFI_D4 = 40
    ROG_MAXIMUS_XI_FORMULA = 41
    ROG_MAXIMUS_X_HERO_WIFI_AC = 42
    ROG_MAXIMUS_Z690_FORMULA = 43
    ROG_MAXIMUS_Z690_HERO = 44
    ROG_MAXIMUS_Z690_EXTREME_GLACIAL = 45
    ROG_STRIX_Z790_I_GAMING_WIFI = 46
    M2N_SLI_Deluxe = 47
    M4A79XTD_EVO = 48
    P5W_DH_Deluxe = 49
    P6T = 50
    P6X58D_E = 51
    P8P67 = 52
    P8P67_EVO = 53
    P8P67_M_PRO = 54
    P8P67_PRO = 55
    P8Z77_V = 56
    P9X79 = 57
    PRIME_X370_PRO = 58
    PRIME_X470_PRO = 59
    PRIME_X570_PRO = 60
    PROART_X570_CREATOR_WIFI = 61
    PRO_WS_X570_ACE = 62
    RAMPAGE_EXTREME = 63
    RAMPAGE_II_GENE = 64
    ROG_MAXIMUS_X_APEX = 65
    ROG_ZENITH_EXTREME = 66
    ROG_ZENITH_II_EXTREME = 67
    TUF_X470_PLUS_GAMING = 68
    Z170_A = 69
    TUF_GAMING_B550M_PLUS_WIFI = 70
    ROG_MAXIMUS_Z790_HERO = 71
    PRIME_Z690_A = 72
    B660GTN = 73
    X670E_Valkyrie = 74
    LP_BI_P45_T2RS_Elite = 75
    LP_DK_P55_T3EH9 = 76
    A890GXM_A = 77
    B350_Gaming_Plus = 78
    B360M_PRO_VDH = 79
    B450A_PRO = 80
    Z270_PC_MATE = 81
    Z77_MS7751 = 82
    Z68_MS7672 = 83
    X570_Gaming_Plus = 84
    X58_SLI_Classified = 85
    X58_3X_SLI = 86
    _965P_S3 = 87
    _970A_UD3 = 88
    AB350_Gaming_3 = 89
    AX370_Gaming_5 = 90
    AX370_Gaming_K7 = 91
    B360_AORUS_GAMING_3_WIFI_CF = 92
    B550_AORUS_PRO = 93
    B560M_AORUS_ELITE = 94
    B560M_AORUS_PRO = 95
    B560M_AORUS_PRO_AX = 96
    B660M_DS3H_AX_DDR4 = 97
    EP45_DS3R = 98
    EP45_UD3R = 99
    EX58_EXTREME = 100
    EX58_UD3R = 101
    G41M_COMBO = 102
    G41MT_S2 = 103
    G41MT_S2P = 104
    H55_USB3 = 105
    H55N_USB3 = 106
    H61M_DS2_REV_1_2 = 107
    H61M_USB3_B3_REV_2_0 = 108
    H67A_UD3H_B3 = 109
    H67A_USB3_B3 = 110
    H81M_HD3 = 111
    B75M_D3H = 112
    MA770T_UD3 = 113
    MA770T_UD3P = 114
    MA785GM_US2H = 115
    MA785GMT_UD2H = 116
    MA78LM_S2H = 117
    MA790X_UD3P = 118
    P35_DS3 = 119
    P35_DS3L = 120
    P55_UD4 = 121
    P55A_UD3 = 122
    P55M_UD4 = 123
    P67A_UD3_B3 = 124
    P67A_UD3R_B3 = 125
    P67A_UD4_B3 = 126
    P8Z68_V_PRO = 127
    X38_DS5 = 128
    X399_AORUS_Gaming_7 = 129
    X58A_UD3R = 130
    X79_UD3 = 131
    Z390_AORUS_ULTRA = 132
    Z390_AORUS_PRO = 133
    Z390_M_GAMING = 134
    Z390_UD = 135
    Z68A_D3H_B3 = 136
    Z68AP_D3 = 137
    Z68X_UD3H_B3 = 138
    Z68X_UD7_B3 = 139
    Z68XP_UD3R = 140
    Z690_AORUS_PRO = 141
    Z690_AORUS_ULTRA = 142
    Z690_GAMING_X_DDR4 = 143
    Z170N_WIFI = 144
    X470_AORUS_GAMING_7_WIFI = 145
    X570_AORUS_MASTER = 146
    X570_GAMING_X = 147
    X570_AORUS_ULTRA = 148
    FH67 = 149
    Unknown = 150


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
