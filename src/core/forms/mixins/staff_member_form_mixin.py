# -*- coding: utf-8 -*-#
from django import forms

from assistant.models import AssistantProxy
from bookkeeper.models import BookkeeperProxy
from manager.models import ManagerProxy


class BWStaffMemberFormMixin(forms.Form):
    """
    A mixin class for staff member forms that handles field removal based on initial data.

    Attributes:
        bookkeeper (forms.ModelChoiceField): A ModelChoiceField for selecting a bookkeeper.
        assistant (forms.ModelChoiceField): A ModelChoiceField for selecting an assistant.
        manager (forms.ModelChoiceField): A ModelChoiceField for selecting a manager.

    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BWStaffMemberFormMixin instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
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

    bookkeeper: forms.ModelChoiceField = forms.ModelChoiceField(
        queryset=BookkeeperProxy.objects.all(), required=False, widget=forms.HiddenInput
    )
    assistant: forms.ModelChoiceField = forms.ModelChoiceField(
        queryset=AssistantProxy.objects.all(), required=False, widget=forms.HiddenInput
    )
    manager: forms.ModelChoiceField = forms.ModelChoiceField(
        queryset=ManagerProxy.objects.all(), required=False, widget=forms.HiddenInput
    )
