# -*- coding: utf-8 -*-#


class CommandStdOutputMixin:
    def stdout_output(self, output_type, msg):
        if output_type == "error":
            self.stdout.write(self.style.ERROR(msg))
        elif output_type == "success":
            self.stdout.write(self.style.SUCCESS(msg))
        elif output_type == "info":
            self.stdout.write(self.style.NOTICE(msg))
        elif output_type == "warn" or output_type == "warning":
            self.stdout.write(self.style.WARNING(msg))
