from pathlib import Path

from PIL import Image
from PIL.ImageQt import ImageQt


def add_check_mark(image_path: Path, check_path: Path):
    image_icon = Image.open(image_path)
    image_icon_access = image_icon.load()
    check = Image.open(check_path)
    check_access = check.load()

    for x in range(check.size[0]):
        for y in range(check.size[1]):
            if check_access[x, y][3] != 0:
                image_icon_access[x, y] = check_access[x, y]

    return ImageQt(image_icon)
