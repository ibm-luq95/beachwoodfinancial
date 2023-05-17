# -*- coding: utf-8 -*-#
from django.views.generic import TemplateView

from core.utils import get_trans_txt


class BWForgetPasswordView(TemplateView):
    template_name = "beach_wood_user/auth/reset_password.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", get_trans_txt("Reset Password"))
        return context