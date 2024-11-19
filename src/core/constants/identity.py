# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _


class LedgerFlareIdentity:
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

    email_address = "ledger_flare@email.com"
    name = _("Ledger Flare")
    url = "https://app.ledgerflare.com/"
    title = _("Ledger Flare - Manage bookkeeping clients with jobs")
    og_title = _("Comprehensive Client Management Platform")
    manager_name = _("Albert Salazar")
    description = _(
        "Manage clients and their associated jobs, tasks, and financial details with our comprehensive platform. With multiple user roles (Bookkeepers, Assistants, Managers) and features like job management, client accounts, briefcase storage, and archived data retrieval, this web application is designed to streamline project workflow and provide a secure centralized location for tracking progress."
    )
    og_description = _(
        "Manage clients and their associated jobs, tasks, and financial details with our comprehensive platform. With multiple user roles (Bookkeepers, Assistants, Managers) and features like job management, client accounts, briefcase storage, and archived data retrieval, this web application is designed to streamline project workflow and provide a secure centralized location for tracking progress."
    )
    keywords = _(
        "Client Management, Job Management, Financial Details, User Roles, Briefcase Feature, Archived Data Retrieval, Scalable Backend Framework (Django), Responsive Frontend Framework (Tailwind CSS with Preline)"
    )
    authos = _("Ibrahim Luqman")
    classification = _("Business & Finance > Accounting & Bookkeeping")
    canonical = "https://www.ledgerflare.com/"
