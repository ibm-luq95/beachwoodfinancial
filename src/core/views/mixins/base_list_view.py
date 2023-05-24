# -*- coding: utf-8 -*-#
import stringcase

from core.utils import debugging_print


class BaseListViewMixin:
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("is_show_created_at", False)
        if hasattr(self.model, "_meta"):
            context.setdefault("app_label", self.model._meta.app_label)
            # context.setdefault("app_label", self.model._meta.model_name)
        if hasattr(self, "model"):
            excluded_fields = ["id", "updated_at", "metadata", "deleted_at", "is_deleted"]
            names_list = [field.name for field in getattr(self.model, "_meta").fields]
            new_list = []
            for name in names_list:
                if name not in excluded_fields:
                    new_list.append(stringcase.sentencecase(name.upper()))

            context.setdefault("fields", new_list)
        return context
