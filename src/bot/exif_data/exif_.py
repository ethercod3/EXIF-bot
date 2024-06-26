from os import getenv, remove
from os.path import join
from typing import Annotated

import exif
from aiogram.types import FSInputFile
from dotenv import load_dotenv

from options import VirtualEnv

load_dotenv()


TextMessage = Annotated[str, "Plain text message"]


def get_exif(path: str) -> tuple[TextMessage]:
    with open(path, "rb") as user_image:
        img = exif.Image(user_image)

        tags = img.list_all()

        message = ""

        for tag in tags:
            try:
                message += f"{tag} : {img.get(tag)}\n"
            except ValueError:
                pass

    if "gps_latitude" in tags and "gps_longitude" in tags:
        lat, long = img.get("gps_latitude"), img.get("gps_longitude")

        if isinstance(lat, tuple):
            lat_dd = float(lat[0]) + float(lat[1]) / 60 + float(lat[2]) / 3600

        if isinstance(long, tuple):
            long_dd = float(long[0]) + float(long[1]) / 60 + float(long[2]) / 3600

        return (message, (lat_dd, long_dd))
    else:
        return (message, (None, None))


def clear_metadata(path, filename) -> FSInputFile:
    with open(path, "rb") as user_image:
        img = exif.Image(user_image)

    img.delete_all()

    clear_path = join(getenv(VirtualEnv.save_file_to), f"cleared_{filename}")

    with open(clear_path, "wb") as clear:
        clear.write(img.get_file())

    remove(path)

    file = FSInputFile(clear_path)

    return file
