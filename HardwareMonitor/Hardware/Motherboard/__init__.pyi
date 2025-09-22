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
    B450M_Pro4_R2_0 = 10
    B450M_Steel_Legend = 11
    B85M_DGS = 12
    Fatal1ty_AB350_Gaming_K4 = 13
    P55_Deluxe = 14
    X399_Phantom_Gaming_6 = 15
    Z77Pro4M = 16
    X570_Pro4 = 17
    X570_Taichi = 18
    X570_Phantom_Gaming_ITX = 19
    Z690_Extreme = 20
    Z690_Steel_Legend = 21
    Z790_Pro_RS = 22
    X570_Phantom_Gaming_4 = 23
    Z790_Taichi = 24
    Z790_Nova_WiFi = 25
    B650M_C = 26
    H61M_DGS = 27
    B850M_STEEL_LEGEND_WIFI = 28
    CROSSHAIR_III_FORMULA = 29
    ROG_CROSSHAIR_VIII_HERO = 30
    ROG_CROSSHAIR_VIII_HERO_WIFI = 31
    ROG_CROSSHAIR_VIII_DARK_HERO = 32
    ROG_CROSSHAIR_VIII_FORMULA = 33
    ROG_CROSSHAIR_VIII_IMPACT = 34
    ROG_STRIX_X470_I = 35
    ROG_CROSSHAIR_X670E_EXTREME = 36
    ROG_CROSSHAIR_X670E_HERO = 37
    ROG_CROSSHAIR_X670E_GENE = 38
    ROG_STRIX_X670E_A_GAMING_WIFI = 39
    ROG_STRIX_X670E_E_GAMING_WIFI = 40
    ROG_STRIX_X670E_F_GAMING_WIFI = 41
    PROART_X670E_CREATOR_WIFI = 42
    ROG_STRIX_X570_E_GAMING = 43
    ROG_STRIX_X570_E_GAMING_WIFI_II = 44
    ROG_STRIX_X570_F_GAMING = 45
    ROG_STRIX_X570_I_GAMING = 46
    ROG_STRIX_B550_E_GAMING = 47
    ROG_STRIX_B550_F_GAMING_WIFI = 48
    ROG_STRIX_B550_I_GAMING = 49
    ROG_STRIX_B760_I_GAMING_WIFI = 50
    ROG_STRIX_Z390_E_GAMING = 51
    ROG_STRIX_Z390_F_GAMING = 52
    ROG_STRIX_Z390_I_GAMING = 53
    ROG_STRIX_Z690_A_GAMING_WIFI_D4 = 54
    ROG_STRIX_B850_I_GAMING_WIFI = 55
    ROG_MAXIMUS_XI_FORMULA = 56
    ROG_MAXIMUS_XII_Z490_FORMULA = 57
    ROG_MAXIMUS_X_HERO_WIFI_AC = 58
    ROG_MAXIMUS_Z690_FORMULA = 59
    ROG_MAXIMUS_Z690_HERO = 60
    ROG_MAXIMUS_Z690_EXTREME_GLACIAL = 61
    ROG_STRIX_Z790_I_GAMING_WIFI = 62
    ROG_STRIX_Z790_E_GAMING_WIFI = 63
    ROG_STRIX_Z790_E_GAMING_WIFI_II = 64
    M2N_SLI_Deluxe = 65
    M4A79XTD_EVO = 66
    P5W_DH_Deluxe = 67
    P6T = 68
    P6X58D_E = 69
    P8P67 = 70
    P8P67_EVO = 71
    P8P67_M_PRO = 72
    P8P67_PRO = 73
    P8Z77_V = 74
    P9X79 = 75
    PRIME_B650_PLUS = 76
    PRIME_X370_PRO = 77
    PRIME_X470_PRO = 78
    PRIME_X570_PRO = 79
    PROART_X570_CREATOR_WIFI = 80
    PRO_WS_X570_ACE = 81
    RAMPAGE_EXTREME = 82
    RAMPAGE_II_GENE = 83
    ROG_MAXIMUS_X_APEX = 84
    ROG_ZENITH_EXTREME = 85
    ROG_ZENITH_II_EXTREME = 86
    TUF_X470_PLUS_GAMING = 87
    Z170_A = 88
    B150M_C = 89
    B150M_C_D3 = 90
    TUF_GAMING_X570_PLUS_WIFI = 91
    TUF_GAMING_B550M_PLUS_WIFI = 92
    ROG_MAXIMUS_Z790_HERO = 93
    ROG_MAXIMUS_Z790_DARK_HERO = 94
    PRIME_Z690_A = 95
    ROG_MAXIMUS_Z790_FORMULA = 96
    ROG_MAXIMUS_XII_HERO_WIFI = 97
    ROG_STRIX_X870_I_GAMING_WIFI = 98
    PRIME_X870_P = 99
    ROG_CROSSHAIR_X870E_APEX = 100
    ROG_CROSSHAIR_X870E_HERO = 101
    ROG_STRIX_X870E_E_GAMING_WIFI = 102
    PROART_X870E_CREATOR_WIFI = 103
    B660GTN = 104
    X670E_Valkyrie = 105
    LP_BI_P45_T2RS_Elite = 106
    LP_DK_P55_T3EH9 = 107
    A890GXM_A = 108
    B350_Gaming_Plus = 109
    B360M_PRO_VDH = 110
    B450A_PRO = 111
    B550A_PRO = 112
    B650M_Gaming_Plus_Wifi = 113
    Z270_PC_MATE = 114
    Z77_MS7751 = 115
    Z68_MS7672 = 116
    X570_Gaming_Plus = 117
    B850M_MORTAR_WIFI = 118
    B850_GAMING_PLUS_WIFI = 119
    B840P_PRO_WIFI = 120
    B850_TOMAHAWK_MAX_WIFI = 121
    B650M_PROJECT_ZERO = 122
    B850P_PRO_WIFI = 123
    B850_EDGE_TI_WIFI = 124
    X870_GAMING_PLUS_WIFI = 125
    X870_TOMAHAWK_WIFI = 126
    X870E_TOMAHAWK_WIFI = 127
    X870E_GODLIKE = 128
    X870P_PRO_WIFI = 129
    X870E_CARBON_WIFI = 130
    X870E_EDGE_TI_WIFI = 131
    Z890_ACE = 132
    Z890_TOMAHAWK_WIFI = 133
    Z890_CARBON_WIFI = 134
    Z890_EDGE_TI_WIFI = 135
    Z890P_PRO_WIFI = 136
    Z890A_PRO_WIFI = 137
    Z890S_PRO_WIFI = 138
    Z890_GAMING_PLUS_WIFI = 139
    Z890S_PRO_WIFI_PROJECT_ZERO = 140
    X58_SLI_Classified = 141
    X58_3X_SLI = 142
    _965P_S3 = 143
    _970A_DS3P = 144
    _970A_UD3 = 145
    AB350_Gaming_3 = 146
    AX370_Gaming_5 = 147
    AX370_Gaming_K7 = 148
    B360M_H = 149
    B360_AORUS_GAMING_3_WIFI_CF = 150
    B550_AORUS_MASTER = 151
    B550_AORUS_PRO = 152
    B550_AORUS_PRO_AC = 153
    B550_AORUS_PRO_AX = 154
    B550_VISION_D = 155
    B550_AORUS_ELITE = 156
    B550_AORUS_ELITE_AX = 157
    B550_GAMING_X = 158
    B550_UD_AC = 159
    B550M_AORUS_PRO = 160
    B550M_AORUS_PRO_AX = 161
    B550M_AORUS_ELITE = 162
    B550M_GAMING = 163
    B550M_DS3H = 164
    B550M_DS3H_AC = 165
    B550M_S2H = 166
    B550M_H = 167
    B550I_AORUS_PRO_AX = 168
    B560M_AORUS_ELITE = 169
    B560M_AORUS_PRO = 170
    B560M_AORUS_PRO_AX = 171
    B560I_AORUS_PRO_AX = 172
    B660_DS3H_DDR4 = 173
    B660_DS3H_AC_DDR4 = 174
    B660M_DS3H_AX_DDR4 = 175
    EP45_DS3R = 176
    EP45_UD3R = 177
    EX58_EXTREME = 178
    EX58_UD3R = 179
    G41M_COMBO = 180
    G41MT_S2 = 181
    G41MT_S2P = 182
    H55_USB3 = 183
    H55N_USB3 = 184
    H61M_DS2_REV_1_2 = 185
    H61M_USB3_B3_REV_2_0 = 186
    H67A_UD3H_B3 = 187
    H67A_USB3_B3 = 188
    H97_D3H = 189
    H81M_HD3 = 190
    B75M_D3H = 191
    MA770T_UD3 = 192
    MA770T_UD3P = 193
    MA785GM_US2H = 194
    MA785GMT_UD2H = 195
    MA78LM_S2H = 196
    MA790X_UD3P = 197
    P35_DS3 = 198
    P35_DS3L = 199
    P55_UD4 = 200
    P55A_UD3 = 201
    P55M_UD4 = 202
    P67A_UD3_B3 = 203
    P67A_UD3R_B3 = 204
    P67A_UD4_B3 = 205
    P8Z68_V_PRO = 206
    X38_DS5 = 207
    X399_AORUS_Gaming_7 = 208
    X58A_UD3R = 209
    X79_UD3 = 210
    Z390_AORUS_ULTRA = 211
    Z390_AORUS_PRO = 212
    Z390_M_GAMING = 213
    Z390_UD = 214
    Z68A_D3H_B3 = 215
    Z68AP_D3 = 216
    Z68X_UD3H_B3 = 217
    Z68X_UD7_B3 = 218
    Z68XP_UD3R = 219
    Z690_AORUS_PRO = 220
    Z690_AORUS_ULTRA = 221
    Z690_AORUS_MASTER = 222
    Z690_GAMING_X_DDR4 = 223
    Z790_AORUS_PRO_X = 224
    Z790_UD = 225
    Z790_UD_AC = 226
    Z790_GAMING_X = 227
    Z790_GAMING_X_AX = 228
    Z170N_WIFI = 229
    B450_AORUS_M = 230
    B450_AORUS_PRO = 231
    B450_GAMING_X = 232
    B450_AORUS_ELITE = 233
    B450M_AORUS_ELITE = 234
    B450M_GAMING = 235
    B450_I_AORUS_PRO_WIFI = 236
    B450M_DS3H = 237
    B450M_S2H = 238
    B450M_H = 239
    B450M_K = 240
    X470_AORUS_GAMING_7_WIFI = 241
    X570_AORUS_MASTER = 242
    X570_AORUS_PRO = 243
    X570_GAMING_X = 244
    X570_AORUS_ULTRA = 245
    B650_AORUS_ELITE = 246
    B650_AORUS_ELITE_AX = 247
    B650_AORUS_ELITE_V2 = 248
    B650_AORUS_ELITE_AX_V2 = 249
    B650_AORUS_ELITE_AX_ICE = 250
    B650_GAMING_X_AX = 251
    B650E_AORUS_ELITE_AX_ICE = 252
    B650M_AORUS_PRO = 253
    B650M_AORUS_PRO_AX = 254
    B650M_AORUS_ELITE = 255
    B650M_AORUS_ELITE_AX = 256
    X670E_AORUS_XTREME = 257
    X870E_AORUS_PRO = 258
    X870E_AORUS_PRO_ICE = 259
    X870E_AORUS_XTREME_AI_TOP = 260
    X870_AORUS_ELITE_WIFI7 = 261
    FH67 = 262
    X11SWN_E = 263
    Unknown = 264


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
