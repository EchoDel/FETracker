from pathlib import Path

from PyQt6.QtWidgets import QApplication

from UI.tracker import MainWindow
from tracker.world_state import WorldState
from emulator_interaction.bizhalk import Emuhawk


icon_folder = Path('UI/IconSets')
emuhawk = Emuhawk(Path('emulator_interaction/controls.json'), 60)

world_state = WorldState(emuhawk)

if __name__ == "__main__":
    app = QApplication([])
    w = MainWindow(world_state, icon_folder)
    w.show()
    app.exec()
