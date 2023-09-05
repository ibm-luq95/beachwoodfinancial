# -*- coding: utf-8 -*-#
from core.forms.mixins.html5_mixin import Html5Mixin
from django import forms


class BWBaseFormMixin(Html5Mixin, forms.Form):
    def __init__(self, *args, **kwargs):
        super(BWBaseFormMixin, self).__init__(*args, **kwargs)
