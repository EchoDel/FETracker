from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon

from pathlib import Path
from PyQt6.QtWidgets import QMainWindow, QPushButton

from tracker.world_state import WorldState
from tracker.keyitems import KeyItems


class MainWindow(QMainWindow):

    def __init__(self, world_state: WorldState, icon_folder: Path):
        self.icon_folder = icon_folder
        self.world_state = world_state

        super(MainWindow, self).__init__()

        self.setWindowTitle("FF4FE Tracker")
        self.setGeometry(400, 400, 300, 260)

        self.icons = {}
        self.setup_icons()

    def setup_icons(self):
        self.world_state.update_key_items()
        obtained_key_items = self.world_state.obtained_key_items
        for i, item in enumerate(KeyItems):
            if item.name in obtained_key_items:
                colour = 'Color'
            else:
                colour = 'Gray'
            print(item.name, [x for x in self.icon_folder.glob(f'**/*{item.name}-{colour}*')])
            btn = QPushButton(self)
            icon = QIcon([str(x) for x in self.icon_folder.glob(f'**/*{item.name}-{colour}*')][0])
            btn.setIcon(icon)
            btn.setStatusTip(item.name)
            btn.setIconSize(QSize(64, 64))
            btn.setBaseSize(80, 80)
            btn.move(80 * i, 0)
            self.icons[item.name] = btn
