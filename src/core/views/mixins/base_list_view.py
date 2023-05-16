# -*- coding: utf-8 -*-#


class BaseListViewMixin:
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("is_show_created_at", False)
        if hasattr(self.model, "_meta"):
            context.setdefault("app_label", self.model._meta.app_label)
            # context.setdefault("app_label", self.model._meta.model_name)
        return context
