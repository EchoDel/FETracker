from enum import Enum
from itertools import chain


class TrackerLocations(Enum):
    """
    Enum which contains the locations of the bytes which stores the information about the checks and found key items
    https://wiki.ff4fe.com/doku.php?id=developer_integration
    """
    Found = [0x1500, 0x1501, 0x1502]
    Used = [0x1503, 0x1504, 0x1505]
    Checked = [0x1510, 0x1511, 0x1512, 0x1513, 0x1514, 0x1515, 0x1516, 0x1517,
               0x1518, 0x1519, 0x151A, 0x151B, 0x151C, 0x151D, 0x151E, 0x151F]
    Locations = [0x7080, 0x7081, 0x7082, 0x7083, 0x7084, 0x7085, 0x7086, 0x7087, 0x7088, 0x7089, 0x708A, 0x708B, 0x708C, 0x708D,
                 0x708E, 0x708F, 0x7090, 0x7091, 0x7092, 0x7093, 0x7094, 0x7095, 0x7096, 0x7097, 0x7098, 0x7099, 0x709A, 0x709B,
                 0x709C, 0x709D, 0x709E, 0x709F, 0x70A0, 0x70A1]


class KeyItems(Enum):
    """
    Enum which contains the locations of the bit which stores if the item has been retrieved or used
    https://wiki.ff4fe.com/doku.php?id=developer_integration
    """
    Package = 0x00
    Sand_Ruby = 0x01
    Legend_Sword = 0x02
    Baron_Key = 0x03
    Twin_Harp = 0x04
    Earth_Crystal = 0x05
    Magma_Key = 0x06
    Tower_Key = 0x07
    Hook = 0x08
    Luca_Key = 0x09
    Darkness_Crystal = 0x0A
    Rat_Tail = 0x0B
    Adamant = 0x0C
    Pan = 0x0D
    Spoon = 0x0E
    Pink_Tail = 0x0F
    Crystal = 0x10


class Kmain(Enum):
    """
    Enum which contains the locations of the bits which stores the information about the checks
    This only contains locations from the Kmain flag
    https://wiki.ff4fe.com/doku.php?id=developer_integration
    """
    Starting_Item = 0x0020
    Antlion_Nest = 0x0021
    Defending_Fabul = 0x0022
    Mt_Ordeals = 0x0023
    Baron_Inn = 0x0024
    Baron_Castle = 0x0025
    Cave_Magnes = 0x0027
    Tower_of_Zot = 0x0028
    Lower_Babil_boss = 0x0029
    Super_Cannon = 0x002A
    Luca = 0x002B
    Sealed_Cave = 0x002C
    Feymarch_Chest = 0x002D
    Rat_Tail_Trade = 0x002E
    Yangs_Wife_Yang = 0x002F
    Yangs_Wife_Pan = 0x0030
    Sylphs = 0x0034  # Hack to get Yangs_Wife_Pan working


Kvanilla = Kmain


class Ksummon(Enum):  # Note Sylphs is in Kmain to make sure Yang's wife works
    """
    Enum which contains the locations of the bits which stores the information about the checks.
    This only contains locations from the Ksummon flag
    https://wiki.ff4fe.com/doku.php?id=developer_integration
    """
    Feymarch_Queen = 0x0031
    Feymarch_King = 0x0032
    Odin_Throne = 0x0033
    Cave_Bahamut = 0x0035


class Kmoon(Enum):
    """
    Enum which contains the locations of the bits which stores the information about the checks
    This only contains locations from the Kmoon flag
    https://wiki.ff4fe.com/doku.php?id=developer_integration
    """
    Murasame_Altar = 0x0036
    Crystal_Sword_Altar = 0x0037
    White_SpearAltar = 0x0038
    Ribbon_Chest_1 = 0x0039
    Ribbon_Chest_2 = 0x003A
    Masamune_Altar = 0x003B


class Ktrap(Enum):
    """
    Enum which contains the locations of the bits which stores the information about the checks
    This only contains locations from the Ktrap flag
    https://wiki.ff4fe.com/doku.php?id=developer_integration
    """
    Tower_of_Zot_Trapped_Chest = 0x003C
    Eblan_trapped_chest_1 = 0x003D
    Eblan_trapped_chest_2 = 0x003E
    Eblan_trapped_chest_3 = 0x003F
    Lower_Babil_Trapped_Chest_1 = 0x0040
    Lower_Babil_Trapped_Chest_2 = 0x0041
    Lower_Babil_Trapped_Chest_3 = 0x0042
    Lower_Babil_Trapped_Chest_4 = 0x0043
    Cave_Eblan_Trapped_Chest = 0x0044
    Upper_Babil_TrappedChest = 0x0045
    Cave_of_Summons_Trapped_chest = 0x0046
    Sylph_Cave_Trapped_Chest_1 = 0x0047
    Sylph_Cave_Trapped_Chest_2 = 0x0048
    Sylph_Cave_Trapped_Chest_3 = 0x0049
    Sylph_Cave_Trapped_Chest_4 = 0x004A
    Sylph_Cave_Trapped_Chest_5 = 0x004B
    Sylph_Cave_Trapped_Chest_6 = 0x004C
    Sylph_Cave_Trapped_Chest_7 = 0x004D
    Giant_of_Babil_Trapped_Chest = 0x004E
    Lunar_Path_Trapped_Chest = 0x004F
    Lunar_Core_Trapped_Chest_1 = 0x0050
    Lunar_Core_Trapped_Chest_2 = 0x0051
    Lunar_Core_Trapped_Chest_3 = 0x0052
    Lunar_Core_Trapped_Chest_4 = 0x0053
    Lunar_Core_Trapped_Chest_5 = 0x0054
    Lunar_Core_Trapped_Chest_6 = 0x0055
    Lunar_Core_Trapped_Chest_7 = 0x0056
    Lunar_Core_Trapped_Chest_8 = 0x0057
    Lunar_Core_Trapped_Chest_9 = 0x0058


class EdwardToroia(Enum):
    """
    Enum which contains the locations of the bits which stores the information about the checks
    This only contains locations from the EdwardToroia which is separate due to the Nkey flag
    https://wiki.ff4fe.com/doku.php?id=developer_integration
    """
    Edward_Toroia = 0x0026


class Nkey(Enum):
    """
    Enum which contains the locations of the bits which stores the information about the checks
    This only contains locations from the Nkey flag
    https://wiki.ff4fe.com/doku.php?id=developer_integration
    """
    Rydia_Mom = 0x0059


AllKeyItems = Enum('AllKeyItems', [(i.name, i.value) for i in chain(Kmain, Kmoon, Ksummon, Ktrap, EdwardToroia, Nkey)])


class CheckRequirements(Enum):
    """
    Enum which contains the information of the required key items before you can get to the check.
    This also include the underground_access, mist_dragon and sylph_1 game progress since there is no key item for this progress
    """
    Starting_Item = None
    Antlion_Nest = None
    Defending_Fabul = None
    Mt_Ordeals = None
    Baron_Inn = None
    Baron_Castle = ['Baron_Key']
    Edward_Toroia = None
    Cave_Magnes = ['Twin_Harp']
    Tower_of_Zot = ['Earth_Crystal']
    Lower_Babil_boss = ['underground_access']
    Super_Cannon = ['underground_access', 'Tower_Key']
    Luca = ['underground_access']
    Sealed_Cave = ['underground_access', 'Luca_Key']
    Feymarch_Chest = ['underground_access']
    Rat_Tail_Trade = ['Hook', 'Rat_Tail']
    Yangs_Wife_Yang = ['sylph_1']
    Yangs_Wife_Pan = ['Sylphs']

    Feymarch_Queen = ['underground_access']
    Feymarch_King = ['underground_access']
    Odin_Throne = ['Baron_Key']
    Sylphs = ['underground_access', 'Pan']
    Cave_Bahamut = ['Darkness_Crystal']

    Murasame_Altar = ['Darkness_Crystal']
    Crystal_Sword_Altar = ['Darkness_Crystal']
    White_SpearAltar = ['Darkness_Crystal']
    Ribbon_Chest_1 = ['Darkness_Crystal']
    Ribbon_Chest_2 = ['Darkness_Crystal']
    Masamune_Altar = ['Darkness_Crystal']

    Rydia_Mom = ['mist_dragon']
