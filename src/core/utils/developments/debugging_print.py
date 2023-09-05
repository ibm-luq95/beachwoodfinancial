# -*- coding: utf-8 -*-#

import traceback
from typing import Any, Optional

from .custom_logger import get_formatted_logger
from ..grab_env_file import grab_env_file

config = grab_env_file()

if config("STAGE_ENVIRONMENT", cast=str) == "DEV":
    from prettyprinter import cpprint
    from termcolor import cprint

logger = get_formatted_logger()

IS_DEBUGGING = config("DEBUG", cast=bool)


def debugging_print(txt_object, **kwargs):
    try:
        from rich import print as rprint
        from rich.pretty import pprint
        from rich import inspect
        from rich.console import Console
        from termcolor import cprint

        console = Console()
        if IS_DEBUGGING is True:
            # var_name = f"{txt_object=}".split("=")
            # cprint(f"######### Variable Name: -> {var_name[0]} <- #########", "yellow", attrs=["bold"])
            if kwargs.get("is_cpprint") is True:
                cpprint(txt_object)
            elif kwargs.get("is_inspect") is True:
                inspect(
                    txt_object,
                    methods=True,
                    all=True,
                    sort=True,
                    help=kwargs.get("help"),
                    private=kwargs.get("private"),
                    title=f"Debugging info for {str(txt_object)} object",
                )
            else:
                # rprint(txt_object)
                pprint(txt_object, expand_all=True)
                # console.log(txt_object)
    except ImportError:
        logger.error("The packages rich or prettyprinter or termcolor not installed!")
        pass
    except Exception as ex:
        logger.error(traceback.format_exc())


def cprint_print(msg: Any, color: str, attrs=None):
    if attrs is None:
        attrs = ["bold"]
    if IS_DEBUGGING is True:
        cprint(msg, color, attrs=attrs)


def get_all_methods(object, is_with_dunder=False) -> list:
    all_methods = []
    for method in dir(object):
        if is_with_dunder is True:
            all_methods.append(method)
        else:
            if not method.startswith("__"):
                all_methods.append(method)
    return all_methods


def debugging_colored_print(
        txt: str,
        fg_color: Optional[str] = "white",
        bg_color: Optional[str] = "white",
        mark: Optional[str] = None,
) -> None:
    # debugging_print(locals())
    try:
        from colorama import init
        from colorama import Fore, Back, Style

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
        bg_colors_map = {
            "red": Back.RED,
            "green": Back.GREEN,
            "yellow": Back.YELLOW,
            "reset": Back.RESET,
            "magenta": Back.MAGENTA,
            "black": Back.BLACK,
            "cyan": Back.CYAN,
            "white": Back.WHITE,
            "blue": Back.BLUE,
        }
        output_txt = fg_colors_map.get(fg_color) + txt + bg_colors_map.get(bg_color)
        if mark is not None:
            mark = mark * 5
            output_txt = (
                    fg_colors_map.get(fg_color)
                    + mark
                    + "  "
                    + txt
                    + "  "
                    + mark
                    + bg_colors_map.get(bg_color)
            )
        print(output_txt)
    except ImportError:
        logger.error("The package colorama not installed!")
