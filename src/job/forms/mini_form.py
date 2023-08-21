# -*- coding: utf-8 -*-#
from typing import Optional
from django import forms
from django.utils import timezone

from django.utils.translation import gettext as _

from beach_wood_user.models import BWUser
from core.choices import JobTypeEnum
from core.constants.file_types_validation import IMAGES_FT
from core.constants.status_labels import CON_NOT_STARTED
from core.forms.mixins.base_form_mixin import BWBaseFormMixin
from core.forms.mixins.js_modal_form_renderer_mixin import BWJSModalFormRendererMixin
from core.forms.mixins.remove_fields_mixin import RemoveFieldsMixin
from core.utils import FileValidator
from job.models.help_messages import JOB_HELP_MESSAGES
from job_category.models import JobCategory

file_validator = FileValidator(max_size=1024 * 1000, content_types=IMAGES_FT)


class JobMiniForm(RemoveFieldsMixin, BWJSModalFormRendererMixin, BWBaseFormMixin):
    def __init__(self, removed_fields: Optional[list] = None, *args, **kwargs):
        super(BWBaseFormMixin, self).__init__(*args, **kwargs)
        RemoveFieldsMixin.__init__(self, removed_fields=removed_fields)
        self.initial["start_date"] = timezone.now().date()
        self.initial["due_date"] = timezone.now().date()
        self.initial["status"] = CON_NOT_STARTED

    title = forms.CharField(label=_("Title"), required=True)
    start_date = forms.DateField(label=_("Start Date"), required=True)
    due_date = forms.DateField(label=_("Due Date"), required=True)
    description = forms.CharField(
        label=_("Description"),
        widget=forms.Textarea(attrs={"placeholder": _("Job content")}),
        required=True,
        help_text=JOB_HELP_MESSAGES.get("description"),
    )
    categories = forms.ModelChoiceField(
        label=_("Categories"),
        widget=forms.CheckboxSelectMultiple,
        queryset=JobCategory.objects.all(),
        # help_text=JOB_HELP_MESSAGES.get("categories"),
    )
    job_type = forms.ChoiceField(
        label=_("Type"),
        choices=JobTypeEnum.choices,
        help_text=JOB_HELP_MESSAGES.get("job_type"),
    )
    managed_by = forms.ModelChoiceField(
        label=_("Manager"),
        required=True,
        queryset=BWUser.objects.all(),
        help_text=JOB_HELP_MESSAGES.get("managed_by"),
    )
    note = forms.CharField(
        label=_("Note"),
        required=False,
        help_text=JOB_HELP_MESSAGES.get("note"),
        widget=forms.TextInput(attrs={"placeholder": _("Optional notes about the job")}),
    )
    client = forms.UUIDField(widget=forms.HiddenInput)
    status = forms.CharField(widget=forms.HiddenInput)