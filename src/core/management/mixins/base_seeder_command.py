# -*- coding: utf-8 -*-#
import traceback
from django.core.management.base import BaseCommand
from abc import ABC, abstractmethod
from django.utils.translation import gettext as _

from core.management.mixins import CommandStdOutputMixin
from faker import Faker


class BaseSeederCommandMixin(ABC, BaseCommand, CommandStdOutputMixin):
    # help = _("")
    FAKER_OBJ = Faker(locale="en_US")

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", "-n", type=str, help=_("Number of records"), required=True
        )

    @abstractmethod
    def handle(self, *args, **options):
        pass
