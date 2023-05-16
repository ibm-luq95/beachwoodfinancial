# -*- coding: utf-8 -*-#
import json
import sys
from enum import Enum, unique, auto


@unique
class ExceptionErrorCodes(Enum):
    ERR_INCORRECT_ERRCODE = (
        auto()
    )  # error code passed is not specified in enum ExceptionErrorCodes
    BOOKKEEPER = "bookkeeper error"
    MANAGER = "manager error"
    ASSISTANT = "assistant error"
    USER = "user error"
    CUSTOM_USER = "custom user error"
    TASKS = "tasks error"
    JOBS = "jobs error"


class BeachWoodFinancialError(Exception):
    """Project exception for all errors in payment app

    Args:
        Exception (Model): Exception Python Exception Class
    """

    def __init__(
            self,
            error_code=None,
            message="",
            data=None,
            is_can_passed=False,
            *args,
            **kwargs
    ):

        # Raise a separate exception in case the error code passed isn't specified in the PaymentErrorCodes enum
        # if not isinstance(error_code, PaymentErrorCodes):
        #     msg = "Error code passed in the error_code param must be of type {0}"
        #     raise PaymentException(
        #         PaymentErrorCodes.ERR_INCORRECT_ERRCODE, msg, PaymentErrorCodes.__class__.__name__
        #     )

        # Set is_can_passed, if passed the exception can pass without rais the error, from where I call the Exception
        self.is_can_passed = is_can_passed
        # Storing the error code on the exception object
        self.error_code = error_code if error_code else "ERR_INCORRECT_ERRCODE"
        separator = " : -> "
        # storing the traceback which provides useful information about where the exception occurred
        self.traceback = sys.exc_info()
        # Storing the extra data for this exception
        # if kwargs.get("is_serialized"):
        self.data = (
            json.dumps(data, default=str) if data else json.dumps("{}", default=str)
        )
        # else:
        #     self.data = data

        # Prefixing the error code to the exception message
        try:
            msg = "[{0}]{1} {2}".format(
                getattr(ExceptionErrorCodes, error_code).value,
                separator,
                message.format(*args, **kwargs),
            )
        except (IndexError, KeyError):
            msg = "[{0}]{1} {2}".format(
                getattr(ExceptionErrorCodes, error_code).value, separator, message
            )
        self.full_error_message = msg
        self.message = msg.split(separator)[-1].strip()
        super().__init__(msg)
