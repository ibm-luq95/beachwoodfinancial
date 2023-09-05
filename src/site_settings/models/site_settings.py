# -*- coding: utf-8 -*-#
from django.contrib.sites.models import Site
from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.utils.translation import gettext as _

from core.models.mixins import BaseModelMixin
from .help_text import HELP_MESSAGES


class SiteSettings(BaseModelMixin):
    """This is web app site settings model

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    slug = models.SlugField(
        _("slug"),
        help_text=HELP_MESSAGES.get("slug"),
        unique=True,
        db_index=True,
        editable=False,
    )
    name = models.CharField(_("name"), max_length=70, help_text=HELP_MESSAGES.get("name"))
    email = models.EmailField(_("email address"), help_text=HELP_MESSAGES.get("email"))
    title = models.CharField(
        _("title"),
        max_length=70,
        help_text=HELP_MESSAGES.get("title"),
        null=True,
        blank=True,
    )
    url = models.URLField(
        _("url"), null=True, blank=True, help_text=HELP_MESSAGES.get("url")
    )
    description = models.TextField(
        _("description"), null=True, blank=True, help_text=HELP_MESSAGES.get("description")
    )
    keywords = models.TextField(
        _("keywords"), null=True, blank=True, help_text=HELP_MESSAGES.get("keywords")
    )
    classification = models.CharField(
        _("classification"),
        max_length=100,
        null=True,
        blank=True,
        help_text=HELP_MESSAGES.get("classification"),
    )
    logo = models.ImageField(
        _("logo"),
        upload_to="app_logo/",
        null=True,
        blank=True,
        help_text=HELP_MESSAGES.get("logo"),
    )
    phone = models.CharField(
        _("phone"),
        max_length=70,
        null=True,
        blank=True,
        help_text=HELP_MESSAGES.get("phone"),
    )
    subject = models.CharField(
        _("subject"),
        max_length=70,
        null=True,
        blank=True,
        help_text=HELP_MESSAGES.get("subject"),
    )
    manager_name = models.CharField(
        _("manager name"),
        max_length=50,
        null=True,
        blank=True,
        help_text=HELP_MESSAGES.get("manager_name"),
    )
    is_closed = models.BooleanField(
        _("is closed"), default=False, help_text=HELP_MESSAGES.get("is_closed")
    )
    close_message = models.TextField(
        _("close message"),
        null=True,
        blank=True,
        help_text=HELP_MESSAGES.get("close_message"),
    )
    can_bookkeepers_login = models.BooleanField(
        _("can bookkeepers login"),
        default=True,
        help_text=HELP_MESSAGES.get("can_bookkeepers_login"),
    )
    can_assistants_login = models.BooleanField(
        _("can assistant login"),
        default=True,
        help_text=HELP_MESSAGES.get("can_assistants_login"),
    )
    site = models.ForeignKey(
        to=Site,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text=HELP_MESSAGES.get("site"),
        db_index=True,
    )
    facebook = models.URLField(
        _("facebook"), null=True, blank=True, help_text=HELP_MESSAGES.get("facebook")
    )
    twitter = models.URLField(
        _("twitter"), null=True, blank=True, help_text=HELP_MESSAGES.get("twitter")
    )
    youtube = models.URLField(
        _("youtube"), null=True, blank=True, help_text=HELP_MESSAGES.get("youtube")
    )
    instagram = models.URLField(
        _("instagram"), null=True, blank=True, help_text=HELP_MESSAGES.get("instagram")
    )
    author = models.CharField(
        _("author"), max_length=50, default="Ibrahim Luqman", editable=False
    )

    class Meta(BaseModelMixin.Meta):
        db_table = "site_settings"

    def __str__(self):
        return _(f"Settings for {self.slug}")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super(SiteSettings, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy("site_settings:web-app-settings")
