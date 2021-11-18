from PyQt6.QtCore import QSize, QObject, pyqtSignal, QThread
from PyQt6.QtGui import QIcon, QPixmap

from pathlib import Path
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel

from UI.helpers import add_check_mark
from UI.locations import IconLocations
from tracker.world_state import WorldState
from tracker.keyitems import KeyItems

icon_size = 64
icon_spacing = 70
background_colour = '#000063'


class Worker(QObject):
    finished = pyqtSignal()  # give worker class a finished signal

    def __init__(self, main_ui, parent=None):
        QObject.__init__(self, parent=parent)
        self.continue_run = True  # provide a bool run condition for the class
        self.main_ui = main_ui

    def do_work(self):
        i = 1
        while self.continue_run:  # give the loop a stoppable condition
            self.main_ui.update_icons()
            self.main_ui.update_labels()
            print(i)
            QThread.sleep(10)
            i = i + 1
        self.finished.emit()  # emit the finished signal when the loop is done

    def stop(self):
        self.continue_run = False  # set the run condition to false on stop


class MainWindow(QMainWindow):
    stop_signal = pyqtSignal()

    def __init__(self, world_state: WorldState, icon_folder: Path):
        self.icon_folder = icon_folder
        self.world_state = world_state

        super(MainWindow, self).__init__()

        self.setWindowTitle("FF4FE Tracker")
        self.setGeometry(400, 400, 800, 400)
        self.setStyleSheet(f"background-color:{background_colour};")

        # Setup the text and other decorations
        self.add_text()

        # Setup the icons for the key items
        self.icons = {}
        self.setup_icons()

        # Setup the icons to be updated
        self.labels = {}
        self.setup_labels()
        self.previous_checks = None

        # Thread:
        self.thread = QThread()
        self.worker = Worker(self)
        self.setup_worker_thread()
        self.thread.start()

    def setup_worker_thread(self):
        self.stop_signal.connect(self.worker.stop)  # connect stop signal to worker stop method
        self.worker.moveToThread(self.thread)

        self.worker.finished.connect(self.thread.quit)  # connect the workers finished signal to stop thread
        self.worker.finished.connect(self.worker.deleteLater)  # connect the workers finished signal to clean up worker
        self.thread.finished.connect(self.thread.deleteLater)  # connect threads finished signal to clean up thread

        self.thread.started.connect(self.worker.do_work)
        self.thread.finished.connect(self.worker.stop)

    def add_text(self):
        label = QLabel('Available Locations', self)
        label.setText('Available Locations')
        label.move(icon_spacing * 6, 0)

    def setup_icons(self):
        self.world_state.update_key_items()
        obtained_key_items = self.world_state.obtained_key_items
        for i, item in enumerate(KeyItems):
            if item.name in obtained_key_items:
                colour = 'Color'
            else:
                colour = 'Gray'
            icon_path = [str(x) for x in self.icon_folder.glob(f'**/*{item.name}-{colour}*')][0]

            btn = QPushButton(self)
            icon = QIcon(icon_path)
            btn.setIcon(icon)
            btn.setStyleSheet(f"background-color:{background_colour};")
            btn.setStatusTip(item.name)
            btn.setIconSize(QSize(icon_size, icon_size))

            button_location = IconLocations[item.name].value
            btn.setMaximumSize(icon_size, icon_size)
            btn.setMinimumSize(icon_size, icon_size)
            btn.move(button_location[1] * icon_spacing, button_location[0] * icon_spacing)
            self.icons[item.name] = btn

    def update_icons(self):
        self.world_state.update_key_items()
        obtained_key_items = self.world_state.obtained_key_items
        for item in KeyItems:
            if item.name in obtained_key_items:
                colour = 'Color'
            else:
                colour = 'Gray'

            icon_path = [str(x) for x in self.icon_folder.glob(f'**/*{item.name}-{colour}*')][0]

            if item.name in [x[0] for x in self.world_state.used_key_items.items() if x[1] == 1]:
                icon_image = add_check_mark(icon_path,
                                            Path('UI/IconSets/checkmark.png'))
                pixmap = QPixmap.fromImage(icon_image)
                icon = QIcon(pixmap)
            else:
                icon = QIcon(icon_path)

            self.icons[item.name].setIcon(icon)

    def setup_labels(self):
        for i in range(20):
            label = QLabel(self)
            label.setText("")
            label.move(icon_spacing * 6, (i + 1) * 30)
            self.labels[i] = label

    def clear_labels(self):
        for key, label in self.labels.items():
            label.clear()

    def update_labels(self):
        available_checks = self.world_state.get_available_checks()
        if self.previous_checks != available_checks:
            self.previous_checks = available_checks
            self.clear_labels()
            for i, check in enumerate(available_checks):
                self.labels[i].setText(check)
