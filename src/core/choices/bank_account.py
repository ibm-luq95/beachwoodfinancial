# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _


class AccountType(models.TextChoices):
    CHECKING_ACCOUNT = "checking_account", _("Checking Account")
    SAVING_ACCOUNT = "saving_account", _("Saving Account")
    CREDITCARD = "credit_card", _("CreditCard")
    LOAN = "loan", _("Loan")
