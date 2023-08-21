from django.core.exceptions import ValidationError
from django.db import transaction
from django import forms

from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

from beach_wood_user.models import BWUser
from core.forms import BaseModelFormMixin, JoditFormMixin
from core.forms.mixins.js_modal_form_renderer_mixin import BWJSModalFormRendererMixin
from core.utils import debugging_print
from job.models import JobProxy


class JobForm(BWJSModalFormRendererMixin, BaseModelFormMixin, JoditFormMixin):
    field_order = [
        "title",
        "client",
        "managed_by",
        "start_date",
        "due_date",
        "description",
        "status",
        "job_type",
        "note",
    ]

    def __init__(
        self,
        bookkeeper=None,
        client=None,
        created_by=None,
        is_updated=False,
        add_jodit_css_class=False,
        *args,
        **kwargs,
    ):
        super(JobForm, self).__init__(*args, **kwargs)
        JoditFormMixin.__init__(self, add_jodit_css_class=add_jodit_css_class)
        if client is not None:
            self.fields["client"].initial = client
        #     self.fields["client"].widget.attrs.update(
        #         {"class": "readonly-select cursor-not-allowed"}
        #     )
        # debugging_print(type(self.initial.get("client")))
        # debugging_print(type(self.initial.get("client").bookkeepers.all()))
        if self.initial.get("client", None) is not None:
            # if is_updated is not True:
            # debugging_print(self.instance.title)
            if hasattr(self.instance.client, "bookkeepers"):
                all_client_bookkeepers = self.instance.client.bookkeepers.all()
                # debugging_print(all_client_bookkeepers)
                bookkeepers_pks = [
                    bookkeeper.user.pk for bookkeeper in all_client_bookkeepers
                ]
                self.fields["managed_by"].queryset = BWUser.objects.filter(
                    pk__in=bookkeepers_pks
                )
                self.fields["managed_by"].help_text = mark_safe(
                    "<strong>Bookkeepers who assigned for this client</strong>"
                )

        self.is_update = is_updated

    def clean_due_date(self):
        data = self.cleaned_data["due_date"]
        now = timezone.now().date()

        if self.is_update is False:
            if data < now:
                raise ValidationError(_("Due date not valid!"), code="invalid")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data

    def save(self, commit=True):
        # Save the provided password in hashed format
        job = super().save(commit=False)
        with transaction.atomic():
            if commit is True:
                job.save()
                self.save_m2m()
        return job

    class Meta(BaseModelFormMixin.Meta):
        model = JobProxy
        widgets = {"categories": forms.CheckboxSelectMultiple}
