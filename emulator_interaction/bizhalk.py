from enum import Enum

import json
import time
from pathlib import Path

from bizhook import Memory

from emulator_interaction.controller import Controller
from tracker.keyitems import TrackerLocations, KeyItems


# http://tasvideos.org/Bizhawk/LuaFunctions/JoypadTableKeyNames.html


def get_status(reader: Memory, locations: list, key_items: Enum) -> dict:
    """
    Performs a number of queries on the memory of bizhook to get the developer data from the emulator.

    :param reader: Memory object from bizhook used to query the ram
    :type reader: Memory
    :param locations: Location in ram to query
    :type locations: list
    :param key_items:
    :type key_items: Enum
    :return: the status of every item within the enum in the games state
    :rtype: dict
    """
    found_bytes = []
    for location in locations:
        found_bytes.append(reader.read_byte(location))

    found_bytes.reverse()
    result = bytes()
    for x in found_bytes:
        result += x

    found_int = int.from_bytes(result, 'big')
    items = {}
    for key_item in key_items:
        items[key_item.name] = found_int >> key_item.value & 1

    return items


class Emuhawk(Controller):
    """
    Class for interacting with a emuhawk emulator using the modified bizhook interface
    https://gitlab.com/EchoDel/bizhook/-/tree/main
    """
    def __init__(self, control_file: Path, frame_rate: int, address: str = '127.0.0.1'):
        super(Emuhawk).__init__()
        self.controls = json.load(open(control_file, 'rb'))
        self.frame_rate = frame_rate
        self.frame_time = 1/self.frame_rate

        self.cartram = Memory('CARTRAM', address)
        self.cartrom = Memory('CARTROM', address)
        self.wram = Memory('WRAM', address)
        self.vram = Memory('VRAM', address)
        self.current_time = time.time()

    def send_command(self, key: str, frames: int):
        """
        Sends the snes controller input to the emulator i.e. 'Left'

        :param key: input button to press
        :type key: int
        :param frames: Number of frames to press for, not this will not be precise but approximate
        :type frames: int
        """
        while frames > 0:
            if time.time() - self.current_time < self.frame_time:
                time.sleep(self.frame_time - (time.time() - self.current_time))
            self.p1_control.set(key)
            self.current_time = time.time()
            frames -= 1

    def get_metadata(self) -> dict:
        """
        Uses the lua interface of bizhawk to query the rom of the emulator to retrieve
        the metadata on the flags ect for the game
        https://wiki.ff4fe.com/doku.php?id=developer_integration

        :return: Dictionary of all the metadata in the rom
        :rtype: dict
        """
        json_doc_start = 0x1FF000
        json_size = self.cartrom.read_int(json_doc_start,
                                          length=4,
                                          endianness='little')

        json_doc = []
        for x in range(json_size):
            json_doc.append(
                self.cartrom.read_byte(json_doc_start + 4 + x).decode('utf-8'))

        return json.loads(''.join(json_doc))

    def get_key_items(self) -> tuple:
        """
        Uses the lua interface of bizhawk to query the wram of the emulator to retrieve
        the current status of the key items.
        https://wiki.ff4fe.com/doku.php?id=developer_integration

        :returns: pair of dicts for the found and used key items
        :rtype: tuple
        """
        # Get the found key items
        found_items = get_status(self.wram, TrackerLocations.Found.value, KeyItems)

        used_items = get_status(self.wram, TrackerLocations.Used.value, KeyItems)

        return found_items, used_items

    def get_checked_locations(self, check_locations: Enum) -> dict:
        """
        Uses the lua interface of bizhawk to query the wram of the emulator to retrieve
        the currently checked and unchecked locations.
        https://wiki.ff4fe.com/doku.php?id=developer_integration

        :param check_locations: Enum of the key item locations to check, helpers.tracker.keyitems
        :type check_locations: Enum

        :return: Status of checked key item locations
        :rtype: dict
        """
        # Get the found key items
        found_items = get_status(self.wram, TrackerLocations.Checked.value, check_locations)

        return found_items
