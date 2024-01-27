from core.choices.fiscal_year import FiscalYearEnum
from core.models.mixins import BaseModelMixin
from django.utils.translation import gettext as _
from django.db import models


class FiscalYear(BaseModelMixin):
    name = models.CharField(_("Name"), max_length=100, null=True, blank=True)
    year = models.PositiveIntegerField(
        _("Year"), db_index=True, unique=True, choices=FiscalYearEnum.choices
    )
    is_current_active = models.BooleanField(
        _("Is current active"), default=False, db_index=True
    )
    description = models.TextField(_("Description"), null=True, blank=True)
