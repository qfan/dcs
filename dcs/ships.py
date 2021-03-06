# This file is generated from pydcs_export.lua

from . import unittype


class Armed_speedboat(unittype.ShipType):
    id = "speedboat"
    name = "Armed speedboat"
    detection_range = 3000
    threat_range = 1000
    air_weapon_dist = 1000


class CVN_70_Carl_Vinson(unittype.ShipType):
    id = "VINSON"
    name = "CVN-70 Carl Vinson"
    plane_num = 72
    helicopter_num = 6
    parking = 4
    detection_range = 30000
    threat_range = 15000
    air_weapon_dist = 15000


class Oliver_Hazzard_Perry_class(unittype.ShipType):
    id = "PERRY"
    name = "Oliver Hazzard Perry class"
    helicopter_num = 2
    parking = 1
    detection_range = 150000
    threat_range = 100000
    air_weapon_dist = 100000


class Ticonderoga_class(unittype.ShipType):
    id = "TICONDEROG"
    name = "Ticonderoga class"
    helicopter_num = 2
    parking = 1
    detection_range = 150000
    threat_range = 100000
    air_weapon_dist = 100000


class FFL_1124_4_Grisha(unittype.ShipType):
    id = "ALBATROS"
    name = "FFL 1124.4 Grisha"
    detection_range = 30000
    threat_range = 16000
    air_weapon_dist = 16000


class CV_1143_5_Admiral_Kuznetsov(unittype.ShipType):
    id = "KUZNECOW"
    name = "CV 1143.5 Admiral Kuznetsov"
    plane_num = 24
    helicopter_num = 12
    parking = 3
    detection_range = 25000
    threat_range = 12000
    air_weapon_dist = 12000


class FSG_1241_1MP_Molniya(unittype.ShipType):
    id = "MOLNIYA"
    name = "FSG 1241.1MP Molniya"
    detection_range = 21000
    threat_range = 2000
    air_weapon_dist = 2000


class CG_1164_Moskva(unittype.ShipType):
    id = "MOSCOW"
    name = "CG 1164 Moskva"
    helicopter_num = 1
    parking = 1
    detection_range = 160000
    threat_range = 75000
    air_weapon_dist = 75000


class FFG_11540_Neustrashimy(unittype.ShipType):
    id = "NEUSTRASH"
    name = "FFG 11540 Neustrashimy"
    helicopter_num = 1
    parking = 1
    detection_range = 27000
    threat_range = 12000
    air_weapon_dist = 12000


class CGN_1144_2_Pyotr_Velikiy(unittype.ShipType):
    id = "PIOTR"
    name = "CGN 1144.2 Pyotr Velikiy"
    helicopter_num = 1
    parking = 1
    detection_range = 250000
    threat_range = 190000
    air_weapon_dist = 190000


class FF_1135M_Rezky(unittype.ShipType):
    id = "REZKY"
    name = "FF 1135M Rezky"
    detection_range = 30000
    threat_range = 16000
    air_weapon_dist = 16000


class Tanker_Elnya_160(unittype.ShipType):
    id = "ELNYA"
    name = "Tanker Elnya 160"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class Dry_cargo_ship_Ivanov(unittype.ShipType):
    id = "Dry-cargo ship-2"
    name = "Dry cargo ship Ivanov"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class Bulk_cargo_ship_Yakushev(unittype.ShipType):
    id = "Dry-cargo ship-1"
    name = "Bulk cargo ship Yakushev"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class Civil_boat_Zvezdny(unittype.ShipType):
    id = "ZWEZDNY"
    name = "Civil boat Zvezdny"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class SSK_877(unittype.ShipType):
    id = "KILO"
    name = "SSK 877"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class SSK_641B(unittype.ShipType):
    id = "SOM"
    name = "SSK 641B"
    detection_range = 0
    threat_range = 0
    air_weapon_dist = 0


class CVN_74_John_C__Stennis(unittype.ShipType):
    id = "Stennis"
    name = "CVN-74 John C. Stennis"
    plane_num = 72
    helicopter_num = 6
    parking = 4
    detection_range = 30000
    threat_range = 15000
    air_weapon_dist = 15000


class LHA_1_Tarawa(unittype.ShipType):
    id = "LHA_Tarawa"
    name = "LHA-1 Tarawa"
    plane_num = 40
    helicopter_num = 36
    parking = 4
    detection_range = 300000
    threat_range = 150000
    air_weapon_dist = 150000


class Type_052B_Destroyer(unittype.ShipType):
    id = "052B"
    name = "Type 052B Destroyer"
    plane_num = 0
    helicopter_num = 1
    parking = 1
    detection_range = 100000
    threat_range = 30000
    air_weapon_dist = 30000


class Type_054A_Frigate(unittype.ShipType):
    id = "054A"
    name = "Type 054A Frigate"
    plane_num = 0
    helicopter_num = 1
    parking = 1
    detection_range = 160000
    threat_range = 45000
    air_weapon_dist = 45000


class Type_052C_Destroyer(unittype.ShipType):
    id = "052C"
    name = "Type 052C Destroyer"
    plane_num = 0
    helicopter_num = 1
    parking = 1
    detection_range = 260000
    threat_range = 100000
    air_weapon_dist = 100000


class LST_Mk_II(unittype.ShipType):
    id = "LST_Mk2"
    name = "LST Mk.II"
    detection_range = 0
    threat_range = 4000
    air_weapon_dist = 4000


class LS_Samuel_Chase(unittype.ShipType):
    id = "USS_Samuel_Chase"
    name = "LS Samuel Chase"
    detection_range = 0
    threat_range = 7000
    air_weapon_dist = 7000


class LCVP__Higgins_boat(unittype.ShipType):
    id = "Higgins_boat"
    name = "LCVP (Higgins boat)"
    detection_range = 3000
    threat_range = 1000
    air_weapon_dist = 1000

ship_map = {
    "speedboat": Armed_speedboat,
    "VINSON": CVN_70_Carl_Vinson,
    "PERRY": Oliver_Hazzard_Perry_class,
    "TICONDEROG": Ticonderoga_class,
    "ALBATROS": FFL_1124_4_Grisha,
    "KUZNECOW": CV_1143_5_Admiral_Kuznetsov,
    "MOLNIYA": FSG_1241_1MP_Molniya,
    "MOSCOW": CG_1164_Moskva,
    "NEUSTRASH": FFG_11540_Neustrashimy,
    "PIOTR": CGN_1144_2_Pyotr_Velikiy,
    "REZKY": FF_1135M_Rezky,
    "ELNYA": Tanker_Elnya_160,
    "Dry-cargo ship-2": Dry_cargo_ship_Ivanov,
    "Dry-cargo ship-1": Bulk_cargo_ship_Yakushev,
    "ZWEZDNY": Civil_boat_Zvezdny,
    "KILO": SSK_877,
    "SOM": SSK_641B,
    "Stennis": CVN_74_John_C__Stennis,
    "LHA_Tarawa": LHA_1_Tarawa,
    "052B": Type_052B_Destroyer,
    "054A": Type_054A_Frigate,
    "052C": Type_052C_Destroyer,
    "LST_Mk2": LST_Mk_II,
    "USS_Samuel_Chase": LS_Samuel_Chase,
    "Higgins_boat": LCVP__Higgins_boat,
}
