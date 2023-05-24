# -*- coding: utf-8 -*-#
from client_category.models import ClientCategory
from core.forms import BaseModelFormMixin


class ClientCategoryForm(BaseModelFormMixin):
    def __init__(self, *args, **kwargs):
        super(ClientCategoryForm, self).__init__(*args, **kwargs)

    class Meta(BaseModelFormMixin.Meta):
        model = ClientCategory
