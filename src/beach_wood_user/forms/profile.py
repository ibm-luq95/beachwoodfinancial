# -*- coding: utf-8 -*-#


from beach_wood_user.models import Profile
from core.forms import BaseModelFormMixin, JoditFormMixin


class ProfileForm(BaseModelFormMixin, JoditFormMixin):
    def __int__(self, add_jodit_css_class=True, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        JoditFormMixin.__init__(self, add_jodit_css_class=add_jodit_css_class)

    class Meta(BaseModelFormMixin.Meta):
        model = Profile
        # widgets = {
        #     "bio": RichHTMLEditorWidget
        # }
