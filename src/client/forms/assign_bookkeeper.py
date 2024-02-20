from typing import Optional

from bookkeeper.models import BookkeeperProxy
from client.models import ClientProxy
from core.forms.mixins.base_form_mixin import BWBaseFormMixin
from django import forms


class AssignBookkeeperForm(BWBaseFormMixin):
    def __init__(self, client: Optional[ClientProxy] = None, *args, **kwargs):
        super(BWBaseFormMixin, self).__init__(*args, **kwargs)
        if client is not None:
            client_bookkeepers = client.bookkeepers.all()
            self.fields.get("bookkeepers").initial = client_bookkeepers

    bookkeepers = forms.ModelMultipleChoiceField(
        queryset=BookkeeperProxy.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
