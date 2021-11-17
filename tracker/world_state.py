from itertools import chain

from emulator_interaction.controller import Controller
from .keyitems import *


class WorldState:
    """
    Class which contains all the code which needed to understand the state of the world. Contains obtained key items,
    current locations, available checks and more.
    """
    def __init__(self, controller: Controller):
        self.controller = controller
        self.flags = {}

        self.underground_access = None
        self.sylph_1 = None
        self.mist_dragon = None

        self.get_metadata = controller.get_metadata
        self.metadata = self.get_metadata()
        self.check_flags()

        # makes an enum for all the possible key item locations in the seed
        key_item_locations = [eval(x) for x in self.flags['K']]
        if 'Nkey' in self.flags['N']:
            key_item_locations.append(Nkey)
        else:
            key_item_locations.append(EdwardToroia)

        self.key_item_locations = Enum('key_item_locations', [(i.name, i.value)
                                                              for i in chain(*key_item_locations)])
        # get the state of all possible key item locations
        self.get_checked_locations = controller.get_checked_locations
        self.location_state, self.check_locations, self.uncheck_locations, self.accessible_checks = None, None, None, None
        self.update_checked_locations()

        self.get_key_items = controller.get_key_items
        self.got_key_items, self.used_key_items, self.obtained_key_items, self.missing_key_items = None, None, None, None
        self.update_key_items()

    def check_flags(self):
        """
        Processes the metadata to split it into each of the different sections in the ff4fe webpage for use in other functions.
        """
        self.flags['other'] = []
        self.flags['kits'] = []
        for flag in self.metadata['flags'].split(' '):
            group = flag[0]
            if group == 'O':
                self.flags['O'] = ['O' + x for x in flag[1:].split('/')]
            elif group == 'K':
                self.flags['K'] = ['K' + x for x in flag[1:].split('/')]
            elif group == 'P':
                self.flags['P'] = flag[1:]
            elif group == 'C':
                self.flags['C'] = ['C' + x for x in flag[1:].split('/')]
            elif group == 'T':
                self.flags['T'] = ['T' + x for x in flag[1:].split('/')]
            elif group == 'S':
                self.flags['S'] = ['S' + x for x in flag[1:].split('/')]
            elif group == 'B':
                self.flags['B'] = ['B' + x for x in flag[1:].split('/')]
            elif group == 'N':
                self.flags['N'] = ['N' + x for x in flag[1:].split('/')]
            elif group == 'E':
                self.flags['E'] = ['E' + x for x in flag[1:].split('/')]
            elif group == 'G':
                self.flags['G'] = ['K' + x for x in flag[1:].split('/')]
            elif group == '-':
                if 'kit' in flag[1:]:
                    self.flags['kits'].append(flag.split(':')[1])
                else:
                    self.flags['other'].append(flag[1:])
            else:
                print(flag)

    def update_checked_locations(self):
        """
        Queries the memory of the emulator to update the class with the status of the key item checks.
        """
        self.location_state = self.get_checked_locations(self.key_item_locations)
        self.check_locations = [key for key, value in self.location_state.items() if value == 1]
        self.uncheck_locations = [key for key, value in self.location_state.items() if value == 0]

    def update_key_items(self):
        """
        Queries the memory of the emulator to update the class with the current key item status.
        """
        self.got_key_items, self.used_key_items = self.get_key_items()
        self.obtained_key_items = [key for key, value in self.got_key_items.items() if value == 1]
        self.missing_key_items = [key for key, value in self.got_key_items.items() if value == 0]

        # add in the underground access since there are two key items we can us
        if ('Hook' in self.obtained_key_items) or ('MagmaKey' in self.obtained_key_items):
            self.underground_access = True
        if self.underground_access:
            self.obtained_key_items.append('underground_access')
        # add the mist dragon and sylph since there is no key item from it
        if self.mist_dragon:
            self.obtained_key_items.append('mist_dragon')
        if self.sylph_1:
            self.obtained_key_items.append('sylph_1')

    def get_available_checks(self) -> list:
        """
        Queries the memory of the emulator to get the list of the currently open unchecked locations.

        :return: Internal names of the unchecked locations
        :rtype: list
        """
        self.update_checked_locations()
        self.accessible_checks = []
        for x in self.key_item_locations:
            missing = False
            # if we have already checked this item then skip over it
            if x.name in self.check_locations:
                continue
            # if there is no gate then add it
            if CheckRequirements[x.name].value is None:
                self.accessible_checks.append(x.name)
            else:
                for gate in CheckRequirements[x.name].value:
                    if gate not in self.obtained_key_items:
                        missing = True
                if not missing:
                    self.accessible_checks.append(x.name)

        return self.accessible_checks

    def get_key_item_locations(self) -> dict:
        """
        Queries the memory of the emulator to find the location each key item was found.

        :return: Location where each key item was found
        :rtype: dict
        """
        result = self.controller.get_found_locations(TrackerLocations.Locations, KeyItems)

        reverse_key_items = {}
        for location in AllKeyItems:
            reverse_key_items[location.value] = location.name

        found_locations = {}
        for x in result.items():
            if x[1] in reverse_key_items:
                found_locations[x[0]] = reverse_key_items[x[1]]

        return found_locations
