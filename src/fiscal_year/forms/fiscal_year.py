from core.forms import BaseModelFormMixin
from fiscal_year.models import FiscalYear


class FiscalYearForm(BaseModelFormMixin):
    class Meta:
        model = FiscalYear
