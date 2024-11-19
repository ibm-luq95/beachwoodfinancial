# -*- coding: utf-8 -*-#
"""Choices package for all apps This package include all choices for all apps."""

__author__ = "Ibrahim Luqman"
__authors__ = [""]
__contact__ = "ibm.luq995@gmail.com"
__copyright__ = "Copyright 5/8/24, BeachwoodFinance, LLC"
__credits__ = ["Ibrahim Luqman"]
__date__ = "5/8/24"
__deprecated__ = False
__email__ = "ibm.luq995@gmail.com"
__license__ = ""
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "2.0"

from .users import BeachWoodUserStatusEnum, BeachWoodUserTypeEnum, BeachWoodUserTypesEnum
from .assistant import AssistantTypeEnum
from .job import JobTypeEnum, JobStatusEnum, JobStateEnum
from .tasks import TaskTypeEnum, TaskStatusEnum
from .bank_account import AccountType
from .company_services import ServiceNameEnum
from .documents import DocumentSectionEnum
from .notes import NoteSectionEnum, NoteStatusEnum
from .important_contact import ImportantContactLabelsEnum
from .client import ClientStatusEnum
from .client_account import ClientAccountStatusEnum
from .general import StatusEnum
