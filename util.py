import os
import platform

def clear_screen() -> None:
    """
    It cleans the screen.
    """

    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')