# -*- coding: utf-8 -*-#
import base64

import traceback

from cryptography.fernet import Fernet
from django.conf import settings

from core.utils import get_formatted_logger

logger = get_formatted_logger()


class PasswordHasher:
    @staticmethod
    def encrypt(pas: str) -> str:
        """Encrypt string password

        Parameters
        ----------
        pas : str
            The password string

        Returns
        -------
        str:
            The encrypted password

        Raises
        ------

        """
        try:
            pas = str(pas)
            cipher_pass = Fernet(settings.ENCRYPT_KEY)
            encrypt_pass = cipher_pass.encrypt(pas.encode("ascii"))
            encrypt_pass = base64.urlsafe_b64encode(encrypt_pass).decode("ascii")
            return encrypt_pass
        except Exception as e:
            logger.error(traceback.format_exc())
            return None

    @staticmethod
    def decrypt(pas: str) -> str:
        """Decrypt password

        Parameters
        ----------
        pas : str
            The encrypted password

        Returns
        -------
        str:
            The encrypted password

        Raises
        ------

        """
        try:
            pas = base64.urlsafe_b64decode(pas)
            # debugging_print(pas)
            cipher_pass = Fernet(settings.ENCRYPT_KEY)
            decod_pass = cipher_pass.decrypt(pas).decode()
            return decod_pass
        except Exception as e:
            logger.error(traceback.format_exc())
            return None
