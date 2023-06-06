# -*- coding: utf-8 -*-#
from django import forms

from client_account.models import ClientAccount
from core.constants.form import EXCLUDED_FIELDS
from core.forms import BaseModelFormMixin
from core.forms.widgets import BWPasswordInputWidget
from core.utils import PasswordHasher


class ClientAccountForm(BaseModelFormMixin):
    def __init__(self, client=None, is_update=False, updated_object=None, *args, **kwargs):
        super(ClientAccountForm, self).__init__(*args, **kwargs)
        self.is_update = is_update
        self.updated_object = updated_object
        if client is not None:
            # print(self.fields.get("client"))
            self.fields["client"].initial = client

    account_password = forms.CharField(widget=BWPasswordInputWidget, required=False)

    def clean_account_password(self):
        data = self.cleaned_data["account_password"]
        if self.is_update is True:
            if not data:
                # debugging_print("No password")
                data = PasswordHasher.encrypt(
                    self.updated_object.decrypted_account_password
                )
            else:
                data = PasswordHasher.encrypt(data)
            # debugging_print(data)
        else:
            data = PasswordHasher.encrypt(data)
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.

        return data

    class Meta(BaseModelFormMixin.Meta):
        model = ClientAccount
        exclude = EXCLUDED_FIELDS
