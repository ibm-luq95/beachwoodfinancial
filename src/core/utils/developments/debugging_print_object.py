from typing import Any, Literal, Optional, List

from django.conf import settings
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.pretty import pprint
from rich.tree import Tree

from core.utils.developments.debugging_print_types import DPOTableOptions


class BWDebuggingPrint:
    """
    A class representing an employee.

    Attributes:
        console (Console): The Console object
        is_debugging (bool): Whether or not debugging is enabled

    Methods:
        print_json(Any) -> None: Print the JSON representation of the object.
        log(Any) -> None: Log the object.
        print(Any) -> None: Print the object.
        pprint(Any) -> None: Print the object using rich pprint.
        rule(text) -> None: Draw a rule.
        print_exception(is_show_locales) -> None: Draw a rule.
        panel(text_content, title: str, subtitle: str) -> None: Draw a panel with content.
        tree(label: str, items: list) -> None: Draw a tree.
        table(columns_headers: list, rows: list, table_options: DPOTableOptions) -> None: Draw a table.
    """

    is_debugging = settings.DEBUG
    console = Console(color_system="truecolor", stderr=True)

    # console = Console(stderr=True)

    def __init__(self):
        try:
            __import__("rich")
        except ImportError:
            print("Rich is not installed!")
        if self.is_debugging is False:
            print("Debugging is not enabled!")

    def print_json(self, obj: Any) -> None:
        """
        Print the given object as JSON.

        Parameters:
            obj (Any): The object to be printed as JSON.

        Returns:
            None
        """
        self.console.print_json(obj)

    @classmethod
    def log(cls, obj: Any) -> None:
        """
        The log() method offers the same capabilities as print, but adds some features useful for debugging a running
        application. Logging writes the current time in a column to the left, and the file and line where the method
        was called to a column on the right.

        Parameters:
            obj (Any): The object to be printed as JSON.

        Returns:
            None
        """
        cls.console.log(obj)

    def print_exception(self, is_show_locales: bool = False) -> None:
        """
        Print the given exception.
        """
        self.console.print_exception(show_locals=is_show_locales)

    @classmethod
    def print(cls, obj: Any, justify: Literal["left", "center", "right"] = "left") -> None:
        """
        Print the given object.
        """
        cls.console.print(obj, justify=justify)

    def rule(self, text: str) -> None:
        """
        Print a rule with the given text.
        """
        self.console.rule(text)

    @classmethod
    def pprint(cls, obj: Any) -> None:
        """
        Pretty print the given object.
        """
        pprint(obj)

    def panel(
        self,
        text_content: Any,
        title: Optional[str] = None,
        subtitle: Optional[str] = None,
    ) -> None:
        """
        Print a panel with the given text.
        """
        print(Panel.fit(text_content, title=title, subtitle=subtitle))

    def table(
        self,
        columns_headers: list,
        rows: List[list],
        table_options: Optional[DPOTableOptions] = None,
        return_table: Optional[bool] = False,
    ) -> None | Table:
        """
        Print a table with the given text.
        """
        if table_options is not None:
            table = Table(**table_options)
        else:
            table = Table()
        for header in columns_headers:
            table.add_column(header, justify="center", no_wrap=True)
        for row in rows:
            table.add_row(*row)

        if return_table is False:
            self.console.print(table)
        else:
            return table

    def tree(self, label: Optional[str] = None, items: Optional[list] = None) -> None:
        """
        Print a tree with the given text.
        """
        tree = Tree(label=label)
        for item in items:
            tree.add(item, highlight=True)
        print(tree)
