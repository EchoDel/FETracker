import time
import sys
from pathlib import Path

from PyQt6.QtGui import QFontDatabase, QFont
from PyQt6.QtWidgets import QApplication

from UI.tracker import MainWindow
from tracker.world_state import WorldState
from emulator_interaction.bizhalk import Emuhawk

# Launch the bizhawk process
import subprocess
from tests.setup_bizhawk import bizhawk_folder


if __name__ == "__main__":
    bizhawk = subprocess.Popen([bizhawk_folder / 'EmuHawk.exe',
                                "--lua=build/lua_components/hook.lua",
                                sys.argv[1]])

    time.sleep(10)

    icon_folder = Path('UI/IconSets')
    emuhawk = Emuhawk(Path('emulator_interaction/controls.json'), 60)

    world_state = WorldState(emuhawk)

    app = QApplication([])

    # Add the font
    fontid = QFontDatabase.addApplicationFont('UI/font/Final_Fantasy_IV_SNES.ttf')
    families = QFontDatabase.applicationFontFamilies(fontid)
    app.setFont(QFont(families[0], 30))

    w = MainWindow(world_state, icon_folder)
    w.show()
    app.exec()
