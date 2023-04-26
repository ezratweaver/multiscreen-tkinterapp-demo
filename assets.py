from pathlib import Path
from tkinter import PhotoImage
from sys import argv
from os import path, chdir

EXE_DIR = path.dirname(argv[0])
chdir(EXE_DIR)

OUTPUT_PATH = EXE_DIR
ASSETS_PATH = OUTPUT_PATH / Path("assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Assets():
    image_button_bg = PhotoImage(
        file=relative_to_assets("button_bg.png"))
    image_firstscreen = PhotoImage(
        file=relative_to_assets("firstscreen.png"))
    image_secondscreen = PhotoImage(
        file=relative_to_assets("secondscreen.png"))
    image_arrow_left = PhotoImage(
        file=relative_to_assets("arrow_left.png"))
    image_arrow_right = PhotoImage(
        file=relative_to_assets("arrow_right.png"))