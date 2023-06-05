# -*- coding: utf-8 -*-#
import stringcase
from django.forms import model_to_dict

from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.general import IS_SHOW_CREATED_AT
from core.utils import debugging_print


class BaseListViewMixin:
    paginate_by = LIST_VIEW_PAGINATE_BY

    # def get_queryset(self) -> dict:
    #     queryset = super().get_queryset()
    #     rows = [model_to_dict(x) for x in queryset]
    #     return rows.pop(0)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("is_show_created_at", IS_SHOW_CREATED_AT)
        if hasattr(self.model, "_meta"):
            context.setdefault("app_label", self.model._meta.app_label)
            # context.setdefault("app_label", self.model._meta.model_name)
        if hasattr(self, "model"):
            excluded_fields = ["id", "updated_at", "metadata", "deleted_at", "is_deleted"]
            # for f in getattr(self.model, "_meta").fields:
            # debugging_print(field.is_relation and field.many_to_many and field.related_name)
            # debugging_print(f.is_relation)
            names_list = [field.name for field in getattr(self.model, "_meta").fields]
            new_list = []
            for name in names_list:
                if name not in excluded_fields:
                    new_list.append(stringcase.sentencecase(name.upper()))

            context.setdefault("fields", new_list)
        return context
