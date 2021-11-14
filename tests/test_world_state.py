import subprocess
import time

import pytest as pytest

from emulator_interaction.bizhalk import Emuhawk
from tracker.world_state import WorldState

from bizhook.export import export_lua_components
from tests.setup_bizhawk import bizhawk_folder

export_lua_components('build')


@pytest.fixture()
def bizhawk():
    # Setup the bizhawk exe
    bizhawk = subprocess.Popen([bizhawk_folder / 'EmuHawk.exe',
                                "--lua=lua_components/hook.lua",
                                "build/FF4FE.bBAQCIBWyAAAAACAriwoAEAAAAAAVcABCqAsAFAAC.KPRBTZVK77.smc"])

    time.sleep(10)
    yield bizhawk

    bizhawk.kill()


@pytest.fixture()
def emuhawk():
    return Emuhawk(60)


def test_world_state(bizhawk, emuhawk):
    WorldState(emuhawk)
