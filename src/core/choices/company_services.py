# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _


class ServiceNameEnum(models.TextChoices):
    OFFICE_365 = "office_365", _("Office 365")
    SUPPORT_SYSTEM = "support_system", _("Support System")
    FOCALBOARD = "focalboard", _("Focalboard System")
    PORTAL_SYSTEM = "portal_system", _("Portal System")
    BOOKKEEPER_CHECKLIST_APP = "bookkeeper_checklist_app", _("Bookkeeper Checklist App")
    QUICKBOOKS_ONLINE = "quickbooks_online", _("Quickbooks Online")
    MAILCHIMP = "mailchimp", _("Mailchimp")
    CRM = "crm", _("CRM")
    BLOG = "blog", _("Blog")
    KENNECTED = "kennected", _("Kennected")
    SHARED_ACCOUNTS = "shared_accounts", _("Shared Accounts")
    BANK_ACCOUNT = "bank_account", _("Bank Account")
    CREDIT_CARD = "credit_card", _("Credit Card")
    PAYROLL = "payroll", _("Payroll")
    POINT_OF_SALE = "point_of_sale", _("Point of Sale")
    MERCHANT_ACCOUNT = "merchant_account", _("Merchant Account")
    OTHER = "other", _("Other")
