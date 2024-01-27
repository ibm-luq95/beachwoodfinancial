# -*- coding: utf-8 -*-#
from typing import Optional

from django import forms
from django.http import HttpRequest
from django.utils.translation import gettext as _

from beach_wood_user.models import BWUser
from client.models import ClientProxy
from client_category.models import ClientCategory
from core.choices import JobStatusEnum, JobTypeEnum, JobStateEnum
from core.choices.fiscal_year import FiscalYearEnum
from core.choices.months import MonthChoices
from core.forms.mixins.base_form_mixin import BWBaseFormMixin
from core.models.querysets import BaseQuerySetMixin
from job_category.models import JobCategory
from reports.forms.mixins.set_initial_form_inputs_mixin import (
    SetInitialFilterFormInputsMixin,
)
from reports.forms.mixins.shared_filters_inputs_mixin import SharedFilterInputsMixin


class ClientJobsFilter(
    BWBaseFormMixin, SharedFilterInputsMixin, SetInitialFilterFormInputsMixin
):
    field_order = ["clients", "categories"]

    def __init__(
        self,
        request: Optional[HttpRequest] = None,
        # qs: Optional[BaseQuerySetMixin] = None,
        *args,
        **kwargs,
    ):
        super(BWBaseFormMixin, self).__init__(*args, **kwargs)
        SetInitialFilterFormInputsMixin.__init__(self, request=request)
        self.fields["created_at"].help_text = _("Client created at")
        self.fields["created_at"].label = _("Client created at")
        self.fields["created_year"].help_text = _("Job created year")
        self.fields.pop("quick_created_at")
        self.fields.pop("created_at")
        # self.fields.pop("created_year")

    clients = forms.ModelMultipleChoiceField(
        label=_("Client"),
        queryset=ClientProxy.objects.order_by("name"),
        required=False,
        # widget=BWFilterSelectMultipleWidget,
        help_text=_("Clients filter"),
    )
    categories = forms.ModelMultipleChoiceField(
        label=_("Client category"),
        queryset=ClientCategory.objects.order_by("name"),
        # widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text=_("Client categories to filter"),
    )
    period_year = forms.ChoiceField(
        label=_("Period year"),
        required=False,
        choices=FiscalYearEnum.choices,
        help_text=_("Period Year"),
    )
    period_month = forms.ChoiceField(
        label=_("Period month"),
        required=False,
        choices=MonthChoices.choices,
        help_text=_("Period Month"),
    )

    job_categories = forms.ModelMultipleChoiceField(
        label=_("Job category"),
        queryset=JobCategory.objects.order_by("name"),
        required=False,
        help_text=_("Filter by job category"),
    )
    job_status = forms.MultipleChoiceField(
        label=_("Job status"),
        required=False,
        choices=JobStatusEnum.choices,
        help_text=_("Filter by job status"),
    )
    job_type = forms.MultipleChoiceField(
        label=_("Job type"),
        required=False,
        choices=JobTypeEnum.choices,
        help_text=_("Filter by job type"),
    )
    job_stats = forms.MultipleChoiceField(
        choices=JobStateEnum.choices,
        label=_("Job state"),
        required=False,
        help_text=_("Filter by job stats"),
    )
    managed_by = forms.ModelMultipleChoiceField(
        queryset=BWUser.objects.all(),
        label=_("Managed by"),
        required=False,
        help_text=_("Filter by staff member manage the job"),
    )
