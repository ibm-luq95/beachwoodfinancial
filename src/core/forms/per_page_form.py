from django import forms
from django.utils.translation import gettext as _

from core.utils.developments.debugging_print_object import BWDebuggingPrint

PER_PAGE_CHOICES = (
    (15, 15),
    (25, 25),
    (50, 50),
    (75, 75),
    (100, 100),
)


class PerPageForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PerPageForm, self).__init__(*args, **kwargs)
        if kwargs.get("initial"):
            self.fields["per_page"].initial = kwargs["initial"].get(
                "per_page", PER_PAGE_CHOICES[0][0]
            )
        else:
            self.fields["per_page"].initial = {"per_page": PER_PAGE_CHOICES[0][0]}

    per_page = forms.ChoiceField(
        choices=PER_PAGE_CHOICES,
        label=_("Per page"),
        help_text=_("Records per page"),
        # initial=50,
        required=False,
    )
