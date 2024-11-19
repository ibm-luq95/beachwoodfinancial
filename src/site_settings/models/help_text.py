# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

HELP_MESSAGES = {
    "slug": _(
        "Site settings code name which indicate the settings section (it must be unique)"
    ),
    "name": _("Web application name"),
    "title": _("Web application title"),
    "og_title": _("Web application title, (it used in SEO)"),
    "email": _("Web application contact email address"),
    "url": _("Web application URL"),
    "og_url": _("Web application URL"),
    "canonical": _("Web application URL"),
    "description": _("Description for the website. (it used in SEO)"),
    "keywords": _("Keywords indicate for the website, separated by (,). (it used in SEO)"),
    "logo": _("Web application logo image"),
    "phone": _("Web application phone number"),
    "manager_name": _("Manager full name"),
    "is_closed": _("Is web application open or close"),
    "close_message": _("Close message which will appear when close"),
    "can_assistants_login": _("Can assistants login to web application"),
    "can_bookkeepers_login": _("Can bookkeepers login to web application"),
    "facebook": _("Facebook URL"),
    "twitter": _("Twitter URL"),
    "youtube": _("Youtube channel URL"),
    "instagram": _("Instagram URL"),
    "site": _("The site this settings related to."),
    "classification": _("Classification for this web app"),
    "subject": _("Website subject"),
    "og_description": _("OG Description"),
}

APPLICATION_CONFIGURATIONS_HELP_MESSAGES = {
    "slug": _("Site settings code name which indicate the settings section"),
    "list_view_paginate_by": _("Default number of rows for table list view"),
    "default_db_string_column_length": _("Default varchar length for string columns"),
    "default_date_time_format": _("Default datetime format"),
    "default_short_truncated_string": _("Default string short truncate string"),
    "default_medium_truncated_string": _("Default string medium truncate string"),
    "default_long_truncated_string": _("Default string long truncate string"),
    "default_short_template_truncated_string": _(
        "Default string short truncate string (for template)"
    ),
    "default_medium_template_truncated_string": _(
        "Default string medium truncate string (for template)"
    ),
    "default_long_template_truncated_string": _(
        "Default string long truncate string (for template)"
    ),
}


SECTION_DESCRIPTIONS_HELP_MESSAGES = {
    "section_title": _("Section title"),
    "description": _("Describe the section functionality"),
    "site": _("The site this settings related to."),
}
