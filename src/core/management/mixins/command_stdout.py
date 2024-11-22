# -*- coding: utf-8 -*-#
"""
File: command_stdout.py
Author: Ibrahim Luqman
Date: 5/13/24

Description: This mixin used in custom command to add stdout functionality to any custom command
"""


class CommandStdOutputMixin:
    """
    A mixin class that provides functionality to capture the standard output of a command.

    """

    def stdout_output(self, output_type, msg):
        if output_type == "error":
            self.stdout.write(self.style.ERROR(msg))
        elif output_type == "success":
            self.stdout.write(self.style.SUCCESS(msg))
        elif output_type == "info":
            self.stdout.write(self.style.NOTICE(msg))
        elif output_type == "warn" or output_type == "warning":
            self.stdout.write(self.style.WARNING(msg))
