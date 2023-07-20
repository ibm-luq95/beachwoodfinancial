# -*- coding: utf-8 -*-#
from colorama import Fore, Style
from colorama import init


def colored_print(**kwargs) -> None:
    """
    Syntax:
        colored_output_with_logging(is_logged=True, text="one two", log_level="error", color="red")

    """
    init(autoreset=True)
    fg_colors_map = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "reset": Fore.RESET,
        "magenta": Fore.MAGENTA,
        "black": Fore.BLACK,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
        "blue": Fore.BLUE,
    }

    color = kwargs.get("color", "yellow")
    text = str(kwargs.get("text", None))
    print(fg_colors_map.get(color) + text)
    print(Style.RESET_ALL)
