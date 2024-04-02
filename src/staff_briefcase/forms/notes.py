# -*- coding: utf-8 -*-#
from typing import Optional

from django import forms
from django.utils.translation import gettext as _

from core.forms.mixins.base_form_mixin import BWBaseFormMixin
from core.forms.mixins.js_modal_form_renderer_mixin import BWJSModalFormRendererMixin
from core.forms.mixins.remove_fields_mixin import RemoveFieldsMixin


class BriefcaseNoteMiniForm(
    RemoveFieldsMixin, BWJSModalFormRendererMixin, BWBaseFormMixin
):
    def __init__(self, removed_fields: Optional[list] = None, *args, **kwargs):
        super(BWBaseFormMixin, self).__init__(*args, **kwargs)
        RemoveFieldsMixin.__init__(self, removed_fields=removed_fields)

    title = forms.CharField(label=_("Title"))
    note = forms.CharField(label=_("Note"), widget=forms.Textarea)
    briefcase = forms.UUIDField(widget=forms.HiddenInput)
