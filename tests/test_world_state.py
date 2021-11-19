import subprocess
import time
from pathlib import Path

import pytest as pytest

from emulator_interaction.bizhalk import Emuhawk
from tracker.world_state import WorldState

from bizhook.export import export_lua_components
from tests.setup_bizhawk import bizhawk_folder

export_lua_components('build')


@pytest.fixture()
def emuhawk():
    emuhawk = Emuhawk(Path('emulator_interaction/controls.json'), 60)
    return emuhawk


def test_starting_state(emuhawk):
    # Setup the bizhawk exe
    bizhawk = subprocess.Popen([bizhawk_folder / 'EmuHawk.exe',
                                "--lua=build/lua_components/hook.lua",
                                "--load-state=tests/FF4FE.bBAQCIBWyAAAAACAriwoAEAAAAAAVcABCqAsAFAAC" +
                                ".KPRBTZVK77.Snes9x.QuickSave1.State",
                                "build/FF4FE.bBAQCIBWyAAAAACAriwoAEAAAAAAVcABCqAsAFAAC.KPRBTZVK77.smc"])

    time.sleep(5)
    world_state = WorldState(emuhawk)
    obtained_key_items = world_state.obtained_key_items
    available_checks = world_state.get_available_checks()
    check_locations = world_state.check_locations
    key_item_locations = world_state.get_key_item_locations()
    bizhawk.kill()
    assert obtained_key_items == ['TwinHarp']
    assert available_checks == ['Antlion_Nest', 'Defending_Fabul', 'Mt_Ordeals', 'Baron_Inn', 'Cave_Magnes']
    assert check_locations == ['Starting_Item']
    assert key_item_locations == {'TwinHarp': 'Starting_Item'}


def test_second_state(emuhawk):
    # Setup the bizhawk exe
    bizhawk = subprocess.Popen([bizhawk_folder / 'EmuHawk.exe',
                                "--lua=build/lua_components/hook.lua",
                                "--load-state=tests/FF4FE.bBAQCIBWyAAAAACAriwoAEAAAAAAVcABCqAsAFAAC" +
                                ".KPRBTZVK77.Snes9x.QuickSave2.State",
                                "build/FF4FE.bBAQCIBWyAAAAACAriwoAEAAAAAAVcABCqAsAFAAC.KPRBTZVK77.smc"])

    time.sleep(10)
    world_state = WorldState(emuhawk)
    obtained_key_items = world_state.obtained_key_items
    available_checks = world_state.get_available_checks()
    check_locations = world_state.check_locations
    key_item_locations = world_state.get_key_item_locations()
    bizhawk.kill()
    assert obtained_key_items == ['TwinHarp', 'TowerKey']
    assert available_checks == ['Defending_Fabul', 'Mt_Ordeals', 'Baron_Inn', 'Cave_Magnes']
    assert check_locations == ['Starting_Item', 'Antlion_Nest']
    assert key_item_locations == {'TwinHarp': 'Starting_Item', 'TowerKey': 'Antlion_Nest'}
