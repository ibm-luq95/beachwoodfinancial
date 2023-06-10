# -*- coding: utf-8 -*-#
from PIL import Image
from django.core import validators
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

from core.choices import ClientStatusEnum
from core.models.mixins import BaseModelMixin
from core.utils import FileValidator
from client_category.models import ClientCategory
from important_contact.models import ImportantContact

file_validator = FileValidator(
    max_size=1024 * 1000,
    content_types=(
        "image/png",
        "image/jpeg",
    ),
)


class Client(BaseModelMixin):
    """This is client model

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    categories = models.ManyToManyField(
        to=ClientCategory, related_name="clients", blank=True
    )
    bookkeepers = models.ManyToManyField(
        to="bookkeeper.BookkeeperProxy", related_name="clients", blank=True
    )
    important_contacts = models.ManyToManyField(
        to=ImportantContact, related_name="client", blank=True
    )
    name = models.CharField(_("name"), max_length=50, null=True)
    email = models.EmailField(_("email"), max_length=50, null=True)
    industry = models.CharField(_("industry"), max_length=50, null=True)
    website = models.URLField(_("website"), null=True, blank=True)
    street = models.CharField(_("street"), max_length=50, null=True, blank=True)
    city = models.CharField(_("city"), max_length=20, null=True, blank=True)
    state = models.CharField(_("state"), max_length=20, null=True, blank=True)
    phone_number = models.CharField(
        _("phone number"), max_length=50, null=True, blank=True
    )
    postcode = models.CharField(
        _("postcode"),
        max_length=10,
        null=True,
        blank=True,
        validators=[validators.integer_validator],
    )
    is_active = models.BooleanField(_("is active"), default=True)
    company_logo = models.ImageField(
        _("company logo"),
        upload_to="logos/",
        null=True,
        blank=True,
        validators=[file_validator],
    )
    status = models.CharField(
        _("status"),
        max_length=10,
        default=ClientStatusEnum.ENABLED,
        choices=ClientStatusEnum.choices,
    )

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        super(Client, self).save(*args, **kwargs)
        if self.company_logo:
            image = Image.open(self.company_logo.path)
            if image.height > 150 or image.width > 150:
                output_size = (150, 150)
                image.thumbnail(output_size)
                image.save(self.company_logo.path)

    def get_total_tasks_for_all_jobs(self) -> int:
        all_tasks_count = []
        if self.jobs.count() <= 0:
            return 0
        for job in self.jobs.all():
            all_tasks_count.append(job.tasks.count())

        return sum(all_tasks_count)  # TODO: check if sum or len to use

    def get_tasks_count(self):
        return self.jobs.all()
