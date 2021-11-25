import subprocess
import time
from pathlib import Path

import pytest as pytest
from PyQt6.QtGui import QFontDatabase, QFont
from PyQt6.QtWidgets import QApplication

from UI.tracker import MainWindow
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
    app = QApplication([])

    # Add the font
    fontid = QFontDatabase.addApplicationFont('UI/font/Final_Fantasy_IV_SNES.ttf')
    families = QFontDatabase.applicationFontFamilies(fontid)
    app.setFont(QFont(families[0], 30))

    icon_folder = Path('UI/IconSets')
    w = MainWindow(world_state, icon_folder)
    w.show()
    app.exec()
    bizhawk.kill()
