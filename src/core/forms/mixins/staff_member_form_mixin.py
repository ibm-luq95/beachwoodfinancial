# -*- coding: utf-8 -*-#
from django import forms

from assistant.models import AssistantProxy
from bookkeeper.models import BookkeeperProxy
from core.utils import debugging_print
from manager.models import ManagerProxy


class BWStaffMemberFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.initial.get("manager") is not None:
            self.fields.pop("bookkeeper")
            self.fields.pop("assistant")
        elif self.initial.get("assistant") is not None:
            self.fields.pop("bookkeeper")
            self.fields.pop("manager")
        elif self.initial.get("bookkeeper") is not None:
            self.fields.pop("assistant")
            self.fields.pop("manager")

    bookkeeper = forms.ModelChoiceField(
        queryset=BookkeeperProxy.objects.all(), required=False, widget=forms.HiddenInput
    )
    assistant = forms.ModelChoiceField(
        queryset=AssistantProxy.objects.all(), required=False, widget=forms.HiddenInput
    )
    manager = forms.ModelChoiceField(
        queryset=ManagerProxy.objects.all(), required=False, widget=forms.HiddenInput
    )
