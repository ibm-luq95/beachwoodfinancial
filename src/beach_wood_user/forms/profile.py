# -*- coding: utf-8 -*-#
from django.forms import ValidationError
from django.utils.translation import gettext as _
import re
from django.core.exceptions import ValidationError


from beach_wood_user.models import Profile
from core.forms import BaseModelFormMixin, JoditFormMixin
from core.forms.widgets import RichHTMLEditorWidget
from core.utils.developments.debugging_print_object import BWDebuggingPrint


class ProfileForm(BaseModelFormMixin, JoditFormMixin):
    def __int__(self, add_jodit_css_class=True, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        JoditFormMixin.__init__(self, add_jodit_css_class=add_jodit_css_class)

    class Meta(BaseModelFormMixin.Meta):
        model = Profile
        # widgets = {
        #     "bio": RichHTMLEditorWidget
        # }
