from django.views.generic import TemplateView
from core.api.throttling import ExportDataRateThrottle
from core.views.mixins import ThrottledViewMixin


class BankRegisterView(ThrottledViewMixin, TemplateView):
    throttle_classes = [ExportDataRateThrottle]
    template_name = "client/bank_register.html"
