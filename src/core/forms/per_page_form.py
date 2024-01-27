from django import forms
from django.utils.translation import gettext as _

PER_PAGE_CHOICES = (
    (25, 25),
    (50, 50),
    (100, 100),
)


class PerPageForm(forms.Form):
    per_page = forms.ChoiceField(
        choices=PER_PAGE_CHOICES,
        label=_("Per page"),
        help_text=_("Per page help text"),
        initial=50
    )
