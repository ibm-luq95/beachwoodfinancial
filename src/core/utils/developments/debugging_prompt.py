from typing import Any, Optional

from rich.prompt import Confirm
from rich.prompt import Prompt


class DebuggingPrompt:
    @staticmethod
    def ask(
        question: str,
        default: Optional[Any] = None,
        choices: Optional[list] = None,
        is_password: Optional[bool] = False,
    ) -> Any:
        """
        Ask a question and prompt for user input.

        Args:
            question (str): The question to ask the user.
            default (Any, optional): The default value if no input is provided. Defaults to None.
            choices (list, optional): The list of choices the user can select from. Defaults to None.
            is_password (bool, optional): Whether the user input should be masked as a password. Defaults to False.

        Returns:
            Any: The user's input.
        """
        return Prompt.ask(question, default=default, choices=choices, password=is_password)

    @staticmethod
    def confirm(question: str) -> Any:
        """
        Static method to confirm a question.

        Args:
            question (str): The question to ask.

        Returns:
            Any: The result of the confirmation.
        """
        return Confirm.ask(question)
