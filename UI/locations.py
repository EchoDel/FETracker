from enum import Enum


class IconLocations(Enum):
    """
    Enum which contains the locations of the bit which stores if the item has been retrieved or used
    https://wiki.ff4fe.com/doku.php?id=developer_integration
    """
    Package = (1, 2)
    SandRuby = (1, 3)
    LegendSword = (3, 1)
    BaronKey = (2, 0)
    TwinHarp = (1, 1)
    EarthCrystal = (1, 0)
    MagmaKey = (2, 1)
    TowerKey = (2, 2)
    Hook = (0, 2)
    LucaKey = (2, 3)
    DarknessCrystal = (0, 3)
    RatTail = (4, 2)
    Adamant = (3, 0)
    Pan = (3, 2)
    Spoon = (3, 3)
    PinkTail = (4, 1)
    Crystal = (0, 0)
    Pass = (0, 1)
