from pathlib import Path

from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QToolButton

from UI.locations import IconLocations


def add_check_mark(image_path: Path, check_path: Path):
    image_icon = Image.open(image_path)
    check = Image.open(check_path)

    final_image = Image.alpha_composite(image_icon, check)

    return ImageQt(final_image)


def setup_button(btn: QToolButton, icon_path: Path, name:str, background_colour: str, icon_size: int, icon_spacing: int):
    icon = QIcon(icon_path)
    btn.setIcon(icon)
    btn.setStyleSheet(f"background-color:{background_colour};")
    btn.setStatusTip(name)
    btn.setIconSize(QSize(icon_size, icon_size))

    # Setup the text settings which are needed to add the found location
    btn.setStyleSheet("color: white;")
    btn.setFont(QFont('Final Fantasy IV SNES', 12))
    btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

    button_location = IconLocations[name].value
    btn.setFixedSize(icon_size * 1.2, icon_size * 1.2)
    btn.move(button_location[1] * icon_spacing, button_location[0] * icon_spacing)
