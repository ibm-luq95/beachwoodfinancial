# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _


class BWIdentity:
    """
    This class represents the identity of Beach Wood Financial.

    Attributes:
    email_address : str
        The email address of Beach Wood Financial.
    name : str
        The name of Beach Wood Financial.
    url : str
        The URL of Beach Wood Financial's website.
    title : str
        The title of Beach Wood Financial's website.
    manager_name : str
        The name of the manager of Beach Wood Financial.
    description : str
        A brief description of Beach Wood Financial.

    """

    email_address = "beach_wood_financial@email.com"
    name = _("Beach Wood Financial")
    url = "https://app.beachwoodfinancial.com/"
    title = _("Beach Wood Financial - Manage bookkeeping clients with jobs")
    manager_name = _("Albert Salazar")
    description = _("")
