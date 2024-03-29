# -*- coding: utf-8 -*-#
import stringcase
from django.contrib.sites.models import Site
from django.forms import model_to_dict

from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.general import IS_SHOW_CREATED_AT, IS_SHOW_LABELS_IN_FILTER_FORM
from core.forms.per_page_form import PerPageForm
from core.utils import debugging_print
from core.utils.developments.debugging_print_object import BWDebuggingPrint
from site_settings.models import SectionDescription


class BWSectionDescriptionHelperMixin:
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        domain = self.request.get_host()
        site_object = Site.objects.filter(domain=domain).first()
        if site_object:
            bw_section_description = SectionDescription.objects.filter(site=site_object)
            bw_section_description_data = dict()
            for item in bw_section_description:
                bw_section_description_data.update({item.section_title: item.description})
            context.setdefault("bw_section_description", bw_section_description_data)
        return context


class BWBaseListViewMixin:
    paginate_by = LIST_VIEW_PAGINATE_BY
    is_show_labels_in_filter_form = IS_SHOW_LABELS_IN_FILTER_FORM

    # def get_queryset(self) -> dict:
    #     queryset = super().get_queryset()
    #     rows = [model_to_dict(x) for x in queryset]
    #     return rows.pop(0)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("is_show_created_at", IS_SHOW_CREATED_AT)
        per_page_number = self.request.GET.get("per_page", LIST_VIEW_PAGINATE_BY)
        per_page_form = PerPageForm(initial={"per_page": per_page_number})
        context.setdefault("per_page_filter_form", per_page_form)
        if hasattr(self, "object_list") is True:
            # for o in self.object_list:
            #     BWDebuggingPrint.pprint(o.status)
            context.setdefault("total_records", len(self.object_list))
        if hasattr(self, "modal"):
            if hasattr(self.model, "_meta"):
                context.setdefault("app_label", self.model._meta.app_label)
                # context.setdefault("app_label", self.model._meta.model_name)
            if hasattr(self, "model"):
                excluded_fields = [
                    "id",
                    "updated_at",
                    "metadata",
                    "deleted_at",
                    "is_deleted",
                ]
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

    def get_paginate_by(self, queryset):
        """
        Paginate by specified value in querystring, or use default class property value.
        """
        # return self.request.GET.get('paginate_by', self.paginate_by)
        per_page_num = self.request.GET.get("per_page", LIST_VIEW_PAGINATE_BY)
        return per_page_num
