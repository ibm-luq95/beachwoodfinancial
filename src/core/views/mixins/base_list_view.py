# -*- coding: utf-8 -*-#
import stringcase
from django.contrib.sites.models import Site

from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.general import IS_SHOW_CREATED_AT, IS_SHOW_LABELS_IN_FILTER_FORM
from core.forms.per_page_form import PerPageForm
from site_settings.models import SectionDescription


class BWSectionDescriptionHelperMixin:
    """
    Mixin class that adds section description data to the context of a view.
    """

    def get_context_data(self, **kwargs):
        """
        Retrieves the context data for the view, including the section description data.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: The context data for the view, including the section description data.

        """
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Get the current domain from the request
        domain = self.request.get_host()

        # Get the site object with the matching domain
        site_object = Site.objects.filter(domain=domain).first()

        if site_object:
            # Get the section description objects for the site
            bw_section_description = SectionDescription.objects.filter(site=site_object)

            # Create a dictionary with the section title as the key and the description as the value
            bw_section_description_data = {
                item.section_title: item.description for item in bw_section_description
            }

            # Add the section description data to the context
            context.setdefault("bw_section_description", bw_section_description_data)

        return context


class BWBaseListViewMixin:
    """
    Mixin class that provides common functionality for list views.

    Attributes:
        paginate_by (int): The number of items to display per page.
        is_show_labels_in_filter_form (bool): Whether to show labels in the filter form.

    Methods:
        get_context_data(**kwargs) -> dict: Retrieves the context data for the view.
        get_paginate_by(queryset) -> int: Paginate by specified value in querystring, or use default class property value.

    """

    paginate_by = LIST_VIEW_PAGINATE_BY
    is_show_labels_in_filter_form = IS_SHOW_LABELS_IN_FILTER_FORM

    def get_context_data(self, **kwargs):
        """
        Retrieves the context data for the view.

        This method adds additional data to the context, such as the value of `is_show_created_at`,
        the `per_page_filter_form`, and the `total_records` if applicable.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: The context data for the view.

        """
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("is_show_created_at", IS_SHOW_CREATED_AT)
        per_page_number = self.request.GET.get("per_page", LIST_VIEW_PAGINATE_BY)
        per_page_form = PerPageForm(initial={"per_page": per_page_number})
        context.setdefault("per_page_filter_form", per_page_form)
        if hasattr(self, "object_list"):
            context.setdefault("total_records", len(self.object_list))
        if hasattr(self, "modal"):
            if hasattr(self.model, "_meta"):
                context.setdefault("app_label", self.model._meta.app_label)
            if hasattr(self, "model"):
                excluded_fields = [
                    "id",
                    "updated_at",
                    "metadata",
                    "deleted_at",
                    "is_deleted",
                ]
                names_list = [field.name for field in getattr(self.model, "_meta").fields]
                new_list = [
                    stringcase.sentencecase(name.upper())
                    for name in names_list
                    if name not in excluded_fields
                ]
                context.setdefault("fields", new_list)
        return context

    def get_paginate_by(self, queryset):
        """
        Paginate by specified value in querystring, or use default class property value.

        Args:
            queryset: The queryset to paginate.

        Returns:
            int: The number of items to display per page.

        """
        per_page_num = self.request.GET.get("per_page", LIST_VIEW_PAGINATE_BY)
        return per_page_num
