# -*- coding: utf-8 -*-#
from django.contrib.sites.models import Site
from django.utils.translation import gettext as _
from django.utils.text import slugify
from core.choices.site_settings import SectionDescriptionEnum
from core.models.mixins import BaseModelMixin, GeneralStatusFieldMixin
from core.utils.grab_env_file import grab_env_file
from django.db import models

from site_settings.models.help_text import SECTION_DESCRIPTIONS_HELP_MESSAGES


class SectionDescription(BaseModelMixin, GeneralStatusFieldMixin):
    """This is descriptions for web app sections, such as jobs, tasks, clients,..etc

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    site = models.ForeignKey(
        to=Site,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text=SECTION_DESCRIPTIONS_HELP_MESSAGES.get("site"),
        db_index=True,
        # editable=False,
    )
    slug = models.SlugField(
        _("slug"),
        help_text=SECTION_DESCRIPTIONS_HELP_MESSAGES.get("slug"),
        # unique=True,
        db_index=True,
        editable=False,
    )
    section_title = models.CharField(
        _("section title"),
        max_length=70,
        help_text=SECTION_DESCRIPTIONS_HELP_MESSAGES.get("section_title"),
        choices=SectionDescriptionEnum.choices,
        db_index=True,
        # unique=True,
    )
    description = models.TextField(
        _("Description"),
        help_text=SECTION_DESCRIPTIONS_HELP_MESSAGES.get("description"),
        null=True,
        blank=True,
    )

    class Meta(BaseModelMixin.Meta):
        db_table = "section_descriptions"
        permissions = [
            ("can_edit_section_descriptions", _("Can edit section descriptions"))
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["site", "section_title"], name="unique_section_title_with_site"
            )
        ]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.section_title)
        config = grab_env_file()
        site_domain = config("SITE_DOMAIN", cast=str)
        site_object = Site.objects.filter(domain=site_domain).first()
        self.site = site_object
        super(SectionDescription, self).save(*args, **kwargs)
