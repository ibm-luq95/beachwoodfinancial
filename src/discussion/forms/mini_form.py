# -*- coding: utf-8 -*-#
from typing import Optional

from django import forms
from django.utils.translation import gettext as _

from core.constants.file_types_validation import IMAGES_AND_DOCS_FT
from core.forms.mixins.base_form_mixin import BWBaseFormMixin
from core.forms.mixins.js_modal_form_renderer_mixin import BWJSModalFormRendererMixin
from core.forms.mixins.remove_fields_mixin import RemoveFieldsMixin
from core.forms.mixins.staff_member_form_mixin import BWStaffMemberFormMixin
from core.utils import FileValidator, debugging_print
from job.models import JobProxy
from special_assignment.models import SpecialAssignmentProxy

file_validator = FileValidator(max_size=1024 * 1000, content_types=IMAGES_AND_DOCS_FT)


class DiscussionMiniForm(
    BWJSModalFormRendererMixin, RemoveFieldsMixin, BWStaffMemberFormMixin, BWBaseFormMixin
):
    def __init__(self, removed_fields: Optional[list] = None, *args, **kwargs):
        super(BWBaseFormMixin, self).__init__(*args, **kwargs)
        BWStaffMemberFormMixin.__init__(self, *args, **kwargs)
        RemoveFieldsMixin.__init__(self, removed_fields=removed_fields)

    body = forms.CharField(label=_("Body"), required=True, widget=forms.Textarea)
    attachment = forms.FileField(
        label=_("Attachment"), required=False, validators=[file_validator]
    )
    job = forms.ModelChoiceField(
        queryset=JobProxy.objects.all(), required=False, widget=forms.HiddenInput
    )
    special_assignment = forms.ModelChoiceField(
        queryset=SpecialAssignmentProxy.objects.all(),
        required=False,
        widget=forms.HiddenInput,
    )
