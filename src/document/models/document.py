# -*- coding: utf-8 -*-#
import secrets

from django.db import models
from django.utils.translation import gettext as _

from core.choices import DocumentSectionEnum
from core.models.mixins.belongs_to_items import BelongsToItemsMixin
from document.models.base_abstract_document import BaseDocumentModel


def saved_document_file_path(instance, filename):
	file_suffix = secrets.token_urlsafe(7)
	return f"documents/{file_suffix}_{filename}"


class Document(BaseDocumentModel, BelongsToItemsMixin):
	document_section = models.CharField(
		_("document section"),
		max_length=15,
		null=True,
		blank=True,
		choices=DocumentSectionEnum.choices,
		editable=False,
	)

	class Meta:
		indexes = [
			models.Index(name="document_section_idx", fields=["document_section"]),
		]

	def save(self, *args, **kwargs):
		if self.job:
			self.document_section = DocumentSectionEnum.JOB
		elif self.task:
			self.document_section = DocumentSectionEnum.TASK
		elif self.client:
			self.document_section = DocumentSectionEnum.CLIENT
		super().save(*args, **kwargs)


# def delete(self, *args, **kwargs):
#     self.document_file.storage.delete(self.document_file.name)
#     super(Documents, self).delete(*args, **kwargs)
