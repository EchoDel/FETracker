from pathlib import Path

from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QToolButton

from UI.locations import IconLocations


def add_check_mark(image_path: str, check_path: Path) -> ImageQt:
    """
    Adds a check mark to the icon passed

    :param image_path: path to the base icon to be adjusted
    :type image_path: str

    :param check_path: path to the checkmark icon
    :type check_path: Path

    :return: Icon with the check mark applied
    :rtype: ImageQt
    """
    image_icon = Image.open(image_path)
    check = Image.open(check_path)

    final_image = Image.alpha_composite(image_icon, check)

    return ImageQt(final_image)


def setup_button(btn: QToolButton, icon_path: str, name: str, background_colour: str, icon_size: int, button_spacing: int):
    """
    Adds all the decorators to the button to setup the basic button style.

    :param btn: The button to decorate
    :param icon_path: Path to the icon .png file
    :param name: name of the item being tracked
    :param background_colour: the background colour of the button
    :param icon_size: The size of the icon
    :param button_spacing: The spacing between the buttons
    :return: None
    """
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
    btn.move(button_location[1] * button_spacing, button_location[0] * button_spacing)
