# -*- encoding: utf-8 -*-
from django.utils.translation import gettext as _
from django.db import models
from django.core import validators

from core.models.mixins import BaseModelMixin
from site_settings.models.help_text import APPLICATION_CONFIGURATIONS_HELP_MESSAGES


class ApplicationConfigurations(BaseModelMixin):
    slug = models.SlugField(
        _("slug"),
        help_text=APPLICATION_CONFIGURATIONS_HELP_MESSAGES.get("slug"),
        unique=True,
        db_index=True,
        editable=False,
        default="app-configs",
    )
    default_date_time_format = models.CharField(
        _("default date time format"),
        max_length=50,
        null=True,
        blank=True,
        help_text=APPLICATION_CONFIGURATIONS_HELP_MESSAGES.get("default_date_time_format"),
        default="jS F Y H:i A",
    )
    list_view_paginate_by = models.IntegerField(
        _("list view paginate by"),
        default=50,
        help_text=APPLICATION_CONFIGURATIONS_HELP_MESSAGES.get("list_view_paginate_by"),
        validators=[validators.integer_validator],
    )
    default_db_string_column_length = models.IntegerField(
        _("default db string column length"),
        default=90,
        help_text=APPLICATION_CONFIGURATIONS_HELP_MESSAGES.get(
            "default_db_string_column_length"
        ),
        validators=[validators.integer_validator],
    )
    default_short_truncated_string = models.IntegerField(
        _("default short truncated string"),
        default=30,
        help_text=APPLICATION_CONFIGURATIONS_HELP_MESSAGES.get(
            "default_short_truncated_string"
        ),
        validators=[validators.integer_validator],
    )
    default_medium_truncated_string = models.IntegerField(
        _("default medium truncated string"),
        default=50,
        help_text=APPLICATION_CONFIGURATIONS_HELP_MESSAGES.get(
            "default_medium_truncated_string"
        ),
        validators=[validators.integer_validator],
    )
    default_long_truncated_string = models.IntegerField(
        _("default long truncated string"),
        default=70,
        help_text=APPLICATION_CONFIGURATIONS_HELP_MESSAGES.get(
            "default_long_truncated_string"
        ),
        validators=[validators.integer_validator],
    )
    default_short_template_truncated_string = models.IntegerField(
        _("default short template truncated string"),
        default=70,
        help_text=APPLICATION_CONFIGURATIONS_HELP_MESSAGES.get(
            "default_short_template_truncated_string"
        ),
        validators=[validators.integer_validator],
    )
    default_medium_template_truncated_string = models.IntegerField(
        _("default medium template truncated string"),
        default=120,
        help_text=APPLICATION_CONFIGURATIONS_HELP_MESSAGES.get(
            "default_medium_template_truncated_string"
        ),
        validators=[validators.integer_validator],
    )
    default_long_template_truncated_string = models.IntegerField(
        _("default long template truncated string"),
        default=200,
        help_text=APPLICATION_CONFIGURATIONS_HELP_MESSAGES.get(
            "default_long_template_truncated_string"
        ),
        validators=[validators.integer_validator],
    )

    class Meta(BaseModelMixin.Meta):
        db_table = "application_configurations"
