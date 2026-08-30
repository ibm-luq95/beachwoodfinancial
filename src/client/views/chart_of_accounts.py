from django.views.generic import TemplateView

from core.api.throttling import ExportDataRateThrottle
from core.views.mixins import ThrottledViewMixin


class ChartOfAccountClientView(ThrottledViewMixin, TemplateView):
    throttle_classes = [ExportDataRateThrottle]
    template_name = "client/chart_of_accounts.html"
