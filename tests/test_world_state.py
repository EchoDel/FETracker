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
def bizhawk():

    yield bizhawk

    bizhawk.kill()


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

    time.sleep(10)
    world_state = WorldState(emuhawk)
    assert world_state.obtained_key_items == ['Twin_Harp']
    assert world_state.get_available_checks() == ['Antlion_Nest', 'Defending_Fabul', 'Mt_Ordeals', 'Baron_Inn', 'Cave_Magnes']
    assert world_state.check_locations == ['Starting_Item']
    bizhawk.kill()


def test_second_state(emuhawk):
    # Setup the bizhawk exe
    bizhawk = subprocess.Popen([bizhawk_folder / 'EmuHawk.exe',
                                "--lua=build/lua_components/hook.lua",
                                "--load-state=tests/FF4FE.bBAQCIBWyAAAAACAriwoAEAAAAAAVcABCqAsAFAAC" +
                                ".KPRBTZVK77.Snes9x.QuickSave2.State",
                                "build/FF4FE.bBAQCIBWyAAAAACAriwoAEAAAAAAVcABCqAsAFAAC.KPRBTZVK77.smc"])

    time.sleep(10)
    world_state = WorldState(emuhawk)
    assert world_state.obtained_key_items == ['Twin_Harp', 'Tower_Key']
    assert world_state.get_available_checks() == ['Defending_Fabul', 'Mt_Ordeals', 'Baron_Inn', 'Cave_Magnes']
    assert world_state.check_locations == ['Starting_Item', 'Antlion_Nest']
    bizhawk.kill()
