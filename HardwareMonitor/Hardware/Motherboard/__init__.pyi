from HardwareMonitor._util.types import IDictionary
from typing import Set


class Manufacturer(int):
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
    Framework = 17
    Fujitsu = 18
    Gateway = 19
    Gigabyte = 20
    HP = 21
    IBM = 22
    Intel = 23
    Jetway = 24
    LattePanda = 25
    Lenovo = 26
    Medion = 27
    Microsoft = 28
    MSI = 29
    NEC = 30
    Pegatron = 31
    Samsung = 32
    Sapphire = 33
    Shuttle = 34
    Sony = 35
    Supermicro = 36
    Toshiba = 37
    XFX = 38
    Zotac = 39
    Unknown = 40


class Model(int):
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
    B550M_Pro4 = 11
    B450M_Steel_Legend = 12
    B85M_DGS = 13
    Fatal1ty_AB350_Gaming_K4 = 14
    P55_Deluxe = 15
    X399_Phantom_Gaming_6 = 16
    Z77Pro4M = 17
    X570_Pro4 = 18
    X570_Taichi = 19
    X570_Phantom_Gaming_ITX = 20
    Z690_Extreme = 21
    Z690_Steel_Legend = 22
    Z790_Pro_RS = 23
    X570_Phantom_Gaming_4 = 24
    Z790_Taichi = 25
    Z790_Nova_WiFi = 26
    B650M_C = 27
    H61M_DGS = 28
    B850M_STEEL_LEGEND_WIFI = 29
    X870E_TAICHI = 30
    X870E_NOVA_WIFI = 31
    CROSSHAIR_III_FORMULA = 32
    ROG_CROSSHAIR_VIII_HERO = 33
    ROG_CROSSHAIR_VIII_HERO_WIFI = 34
    ROG_CROSSHAIR_VIII_DARK_HERO = 35
    ROG_CROSSHAIR_VIII_FORMULA = 36
    ROG_CROSSHAIR_VIII_IMPACT = 37
    ROG_STRIX_X470_I = 38
    ROG_CROSSHAIR_X670E_EXTREME = 39
    ROG_CROSSHAIR_X670E_HERO = 40
    ROG_CROSSHAIR_X670E_GENE = 41
    ROG_STRIX_X670E_A_GAMING_WIFI = 42
    ROG_STRIX_X670E_E_GAMING_WIFI = 43
    ROG_STRIX_X670E_F_GAMING_WIFI = 44
    PROART_X670E_CREATOR_WIFI = 45
    ROG_STRIX_X570_E_GAMING = 46
    ROG_STRIX_X570_E_GAMING_WIFI_II = 47
    ROG_STRIX_X570_F_GAMING = 48
    ROG_STRIX_X570_I_GAMING = 49
    ROG_STRIX_B550_E_GAMING = 50
    ROG_STRIX_B550_F_GAMING_WIFI = 51
    ROG_STRIX_B550_I_GAMING = 52
    ROG_STRIX_B760_I_GAMING_WIFI = 53
    ROG_STRIX_Z390_E_GAMING = 54
    ROG_STRIX_Z390_F_GAMING = 55
    ROG_STRIX_Z390_I_GAMING = 56
    ROG_STRIX_Z690_A_GAMING_WIFI_D4 = 57
    ROG_STRIX_Z690_G_GAMING_WIFI = 58
    ROG_STRIX_B850_E_GAMING_WIFI = 59
    ROG_STRIX_B850_I_GAMING_WIFI = 60
    ROG_MAXIMUS_XI_FORMULA = 61
    ROG_MAXIMUS_XII_Z490_FORMULA = 62
    ROG_MAXIMUS_X_HERO_WIFI_AC = 63
    ROG_MAXIMUS_Z690_FORMULA = 64
    ROG_MAXIMUS_Z690_HERO = 65
    ROG_MAXIMUS_Z690_EXTREME_GLACIAL = 66
    ROG_STRIX_Z790_I_GAMING_WIFI = 67
    ROG_STRIX_Z790_E_GAMING_WIFI = 68
    ROG_STRIX_Z790_E_GAMING_WIFI_II = 69
    M2N_SLI_Deluxe = 70
    M4A79XTD_EVO = 71
    P5W_DH_Deluxe = 72
    P6T = 73
    P6X58D_E = 74
    P8P67 = 75
    P8P67_EVO = 76
    P8P67_M_PRO = 77
    P8P67_PRO = 78
    P8Z77_V = 79
    P9X79 = 80
    PRIME_B650_PLUS = 81
    PRIME_X370_PRO = 82
    PRIME_X470_PRO = 83
    PRIME_X570_PRO = 84
    PROART_X570_CREATOR_WIFI = 85
    PRO_WS_X570_ACE = 86
    RAMPAGE_EXTREME = 87
    RAMPAGE_II_GENE = 88
    ROG_MAXIMUS_X_APEX = 89
    ROG_ZENITH_EXTREME = 90
    ROG_ZENITH_II_EXTREME = 91
    TUF_X470_PLUS_GAMING = 92
    TUF_GAMING_X870_PLUS_WIFI = 93
    Z170_A = 94
    Z170_PRO_GAMING = 95
    B150M_C = 96
    B150M_C_D3 = 97
    TUF_GAMING_X570_PLUS_WIFI = 98
    TUF_GAMING_B550M_PLUS_WIFI = 99
    TUF_GAMING_B760M_PLUS_WIFI_D4 = 100
    ROG_MAXIMUS_Z790_HERO = 101
    ROG_MAXIMUS_Z790_DARK_HERO = 102
    PRIME_Z690_A = 103
    ROG_MAXIMUS_Z790_FORMULA = 104
    ROG_MAXIMUS_XII_HERO_WIFI = 105
    ROG_STRIX_X870_I_GAMING_WIFI = 106
    PRIME_X870_P = 107
    ROG_CROSSHAIR_X870E_APEX = 108
    ROG_CROSSHAIR_X870E_HERO = 109
    ROG_CROSSHAIR_X870E_DARK_HERO = 110
    ROG_STRIX_X870E_E_GAMING_WIFI = 111
    PROART_X870E_CREATOR_WIFI = 112
    PROART_B760_CREATOR_D4 = 113
    TUF_GAMING_B450_PLUS_II = 114
    TUF_GAMING_B850M_PLUS_II = 115
    B660GTN = 116
    X670E_Valkyrie = 117
    LP_BI_P45_T2RS_Elite = 118
    LP_DK_P55_T3EH9 = 119
    A890GXM_A = 120
    B350_Gaming_Plus = 121
    B360M_PRO_VDH = 122
    B450A_PRO = 123
    B550A_PRO = 124
    B650M_Gaming_Plus_Wifi = 125
    Z270_PC_MATE = 126
    Z77_MS7751 = 127
    Z68_MS7672 = 128
    X570_Gaming_Plus = 129
    X570_MS7C35 = 130
    B850M_MORTAR = 131
    B850M_MORTAR_WIFI = 132
    B850_GAMING_PLUS_WIFI = 133
    B850_GAMING_PLUS_WIFI6E = 134
    B850_GAMING_PLUS_WIFI_PZ = 135
    B850M_GAMING_PLUS_WIFI = 136
    B850M_GAMING_PLUS_WIFI6E = 137
    B840P_PRO_WIFI = 138
    B840M_GAMING_PLUS_WIFI6E = 139
    B850_TOMAHAWK_WIFI = 140
    B850_TOMAHAWK_MAX_WIFI = 141
    B650M_PROJECT_ZERO = 142
    B850P_PRO_WIFI = 143
    B850MA_PRO_WIFI = 144
    B850MA_PRO_WIFI_PZ = 145
    B850MP_PRO_WIFI = 146
    B850_EDGE_TI_WIFI = 147
    B850I_EDGE_TI_WIFI = 148
    B850MPOWER = 149
    X870_GAMING_PLUS_WIFI = 150
    X870E_GAMING_PLUS_WIFI = 151
    X870_TOMAHAWK_WIFI = 152
    X870E_TOMAHAWK_WIFI = 153
    X870E_TOMAHAWK_MAX_WIFI_PZ = 154
    X870E_GODLIKE = 155
    X870P_PRO_WIFI = 156
    X870EP_PRO_WIFI = 157
    X870E_CARBON_WIFI = 158
    X870E_EDGE_TI_WIFI = 159
    X870E_ACE_MAX = 160
    Z790_GODLIKE_MAX = 161
    Z890_ACE = 162
    Z890_TOMAHAWK_WIFI = 163
    Z890_CARBON_WIFI = 164
    Z890_EDGE_TI_WIFI = 165
    Z890_UNIFY_X = 166
    Z890I_EDGE_TI_WIFI = 167
    Z890P_PRO_WIFI = 168
    Z890A_PRO_WIFI = 169
    Z890S_PRO_WIFI = 170
    Z890_GAMING_PLUS_WIFI = 171
    Z890S_PRO_WIFI_PROJECT_ZERO = 172
    B850S_PRO_WIFI6E = 173
    Z390_GAMING_EDGE_AC = 174
    X58_SLI_Classified = 175
    X58_3X_SLI = 176
    _965P_S3 = 177
    _970A_DS3P = 178
    _970A_UD3 = 179
    AB350_Gaming_3 = 180
    AX370_Gaming_5 = 181
    AX370_Gaming_K7 = 182
    A320M_S2H_CF = 183
    B360M_H = 184
    B360_AORUS_GAMING_3_WIFI_CF = 185
    B550_AORUS_MASTER = 186
    B550_AORUS_PRO = 187
    B550_AORUS_PRO_AC = 188
    B550_AORUS_PRO_AX = 189
    B550_VISION_D = 190
    B550_AORUS_ELITE = 191
    B550_AORUS_ELITE_AX = 192
    B550_GAMING_X = 193
    B550_UD_AC = 194
    B550M_AORUS_PRO = 195
    B550M_AORUS_PRO_AX = 196
    B550M_AORUS_ELITE = 197
    B550M_GAMING = 198
    B550M_DS3H = 199
    B550M_DS3H_AC = 200
    B550M_S2H = 201
    B550M_H = 202
    B550I_AORUS_PRO_AX = 203
    B560M_AORUS_ELITE = 204
    B560M_AORUS_PRO = 205
    B560M_AORUS_PRO_AX = 206
    B560I_AORUS_PRO_AX = 207
    B650_EAGLE_AX = 208
    B660_DS3H_DDR4 = 209
    B660_DS3H_AC_DDR4 = 210
    B660M_DS3H_AX_DDR4 = 211
    EP45_DS3R = 212
    EP45_UD3R = 213
    EX58_EXTREME = 214
    EX58_UD3R = 215
    G41M_COMBO = 216
    G41MT_S2 = 217
    G41MT_S2P = 218
    H55_USB3 = 219
    H55N_USB3 = 220
    H61M_DS2_REV_1_2 = 221
    H61M_USB3_B3_REV_2_0 = 222
    H67A_UD3H_B3 = 223
    H67A_USB3_B3 = 224
    H97_D3H = 225
    H81M_HD3 = 226
    B75M_D3H = 227
    MA770T_UD3 = 228
    MA770T_UD3P = 229
    MA785GM_US2H = 230
    MA785GMT_UD2H = 231
    MA78LM_S2H = 232
    MA790X_UD3P = 233
    MA790X_DS4 = 234
    P35_DS3 = 235
    P35_DS3L = 236
    P55_UD4 = 237
    P55A_UD3 = 238
    P55M_UD4 = 239
    P67A_UD3_B3 = 240
    P67A_UD3R_B3 = 241
    P67A_UD4_B3 = 242
    P8Z68_V_PRO = 243
    X38_DS5 = 244
    X399_AORUS_Gaming_7 = 245
    X58A_UD3R = 246
    X79_UD3 = 247
    Z390_AORUS_ULTRA = 248
    Z390_AORUS_PRO = 249
    Z390_M_GAMING = 250
    Z390_UD = 251
    Z68A_D3H_B3 = 252
    Z68AP_D3 = 253
    Z68X_UD3H_B3 = 254
    Z68X_UD7_B3 = 255
    Z68XP_UD3R = 256
    Z690_AORUS_PRO = 257
    Z690_AORUS_ULTRA = 258
    Z690_AORUS_MASTER = 259
    Z690_GAMING_X_DDR4 = 260
    Z790_AORUS_PRO_X = 261
    Z790_UD = 262
    Z790_UD_AC = 263
    Z790_GAMING_X = 264
    Z790_GAMING_X_AX = 265
    Z170N_WIFI = 266
    B450_AORUS_M = 267
    B450_AORUS_PRO = 268
    B450_GAMING_X = 269
    B450_AORUS_ELITE = 270
    B450M_AORUS_ELITE = 271
    B450M_GAMING = 272
    B450_I_AORUS_PRO_WIFI = 273
    B450M_DS3H = 274
    B450M_S2H = 275
    B450M_H = 276
    B450M_K = 277
    X470_AORUS_GAMING_7_WIFI = 278
    X570_AORUS_MASTER = 279
    X570_AORUS_PRO = 280
    X570_GAMING_X = 281
    X570_AORUS_ULTRA = 282
    B650_AORUS_ELITE = 283
    B650_AORUS_ELITE_AX = 284
    B650_AORUS_ELITE_V2 = 285
    B650_AORUS_ELITE_AX_V2 = 286
    B650_AORUS_ELITE_AX_ICE = 287
    B650_GAMING_X_AX = 288
    B650E_AORUS_ELITE_AX_ICE = 289
    B650M_AORUS_PRO = 290
    B650M_AORUS_PRO_AX = 291
    B650M_AORUS_ELITE = 292
    B650M_AORUS_ELITE_AX = 293
    B650I_AX = 294
    X670E_AORUS_XTREME = 295
    X870E_AORUS_PRO = 296
    X870E_AORUS_PRO_ICE = 297
    X870E_AORUS_XTREME_AI_TOP = 298
    X870_AORUS_ELITE_WIFI7 = 299
    X870_AORUS_ELITE_WIFI7_ICE = 300
    X670_AORUS_ELITE_AX = 301
    FH67 = 302
    X11SWN_E = 303
    FRANBMCP03 = 304
    FRANBMCP06 = 305
    FRANBMCP08 = 306
    FRANBMCP0A = 307
    FRANBMCP0B = 308
    FRANBMCP0C = 309
    FRANGACP04 = 310
    FRANGACP06 = 311
    FRANGACP08 = 312
    FRANMACP04 = 313
    FRANMACP06 = 314
    FRANMACP08 = 315
    FRANMBCP04 = 316
    FRANMCCP04 = 317
    FRANMCCP06 = 318
    FRANMCCP07 = 319
    FRANMDCP05 = 320
    FRANMDCP07 = 321
    FRANMECP02 = 322
    FRANMECP05 = 323
    FRANMECP06 = 324
    FRANMZCP07 = 325
    FRANMZCP09 = 326
    FRANMFCP02 = 327
    FRANMFCP04 = 328
    FRANMFCP06 = 329
    FRAPMACP03 = 330
    FRAPMACP05 = 331
    FRANMGCP05 = 332
    FRANMGCP07 = 333
    FRANMGCP09 = 334
    Unknown = 335


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
