# -*- coding: utf-8 -*-#
from django.core import validators
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# from client.models import Client
from core.choices import ImportantContactLabelsEnum
from core.models.mixins import BaseModelMixin


class ImportantContact(BaseModelMixin):
    """Important contact for client

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    contact_label = models.CharField(
        _("contact label"),
        max_length=20,
        choices=ImportantContactLabelsEnum.choices,
        db_index=True,
    )
    company_name = models.CharField(
        _("company name"), max_length=60, null=True, blank=True
    )
    contact_description = models.TextField(_("description"), null=True, blank=True)
    contact_first_name = models.CharField(_("first name"), max_length=50, null=False)
    contact_last_name = models.CharField(_("last name"), max_length=50, null=False)
    contact_email = models.EmailField(_("contact email"), null=False, unique=True)
    contact_city = models.CharField(_("city"), max_length=50, null=True, blank=True)
    contact_state = models.CharField(_("state"), max_length=50, null=True, blank=True)
    contact_postcode = models.CharField(
        _("postcode"),
        max_length=10,
        null=True,
        blank=True,
        validators=[validators.integer_validator],
    )
    contact_phone = models.CharField(_("phone"), max_length=80, null=False, blank=True)
    contact_website = models.URLField(_("website"), null=True, blank=True)
    contact_notes = models.TextField(_("notes"), null=True, blank=True)
    custom_fields = models.JSONField(_("custom_fields"), null=True, blank=True)

    def __str__(self):
        # return f"Contact {self.contact_label} for client {self.client}"
        return f"{self.get_contact_label_display()} - {self.company_name}"

    @property
    def full_name(self) -> str:
        return f"{self.contact_first_name} {self.contact_last_name}"

    # def get_absolute_url(self):
    #     return reverse("important_contact:manager:update", kwargs={"pk": self.pk})

    @property
    def contact_fullname(self):
        return f"{self.contact_first_name} {self.contact_last_name}"
