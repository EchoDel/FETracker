import time


class Controller:
    """
    Stub of a class to enable the controllers to be referenced as type hints
    """

    def sleep(self, frames: int):
        """
        Method which sleeps for a number of frames. Note this will not in the Controller class
        since it needs a frame_time which does not exist.

        Each class implements its own interactions with the emulator

        :param frames: Number of frames to sleep for, not this will not be precise but approximate
        :type frames: int
        """
        time.sleep(frames * self.frame_time)

    def get_metadata(self) -> dict:
        """
        Stub of a method which interacts with the memory of the emulator to retrieve the metadata from the ff4fe rom.
        https://wiki.ff4fe.com/doku.php?id=developer_integration

        Each class implements its own interactions with the emulator

        :returns: Dictionary of all the metadata in the rom
        :rtype: dict
        """
        pass

    def get_key_items(self) -> tuple:
        """
        Stub of a method which interacts with the memory of the emulator to retrieve the key item state.
        https://wiki.ff4fe.com/doku.php?id=developer_integration

        Each class implements its own interactions with the emulator

        :returns: pair of dicts for the found and used key items
        :rtype: tuple
        """
        pass

    def get_checked_locations(self, check_locations) -> dict:
        """
        Stub of a method which interacts with the memory of the emulator to retrieve the checked key items.
        https://wiki.ff4fe.com/doku.php?id=developer_integration

        Each class implements its own interactions with the emulator

        :param check_locations: Enum of the key item locations to check, helpers.tracker.keyitems
        :type check_locations: Enum

        :return: Status of checked key item locations
        :rtype: dict
        """
        pass
