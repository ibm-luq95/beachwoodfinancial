from colorama import init
from colorama import Fore, Back, Style

from core.utils import get_formatted_logger

logger = get_formatted_logger()


def colored_output_with_logging(**kwargs) -> None:
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
    is_logged = kwargs.get("is_logged", False)
    log_level = kwargs.get("log_level", "warning")
    color = kwargs.get("color", "yellow")
    text = kwargs.get("text", None)
    if is_logged is True:
        getattr(logger, log_level)(fg_colors_map.get(color) + text)
    else:
        print(fg_colors_map.get(color) + text)
    print(Style.RESET_ALL)
