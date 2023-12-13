import secrets

from django.db import models
from django.utils.translation import gettext as _

from core.constants.file_types_validation import IMAGES_AND_DOCS_FT
from core.models.mixins import BaseModelMixin, StrModelMixin, GeneralStatusFieldMixin
from core.utils import FileValidator

file_validator = FileValidator(max_size=1024 * 1000, content_types=IMAGES_AND_DOCS_FT)


def saved_document_file_path(instance, filename):
	file_suffix = secrets.token_urlsafe(7)
	return f"documents/{file_suffix}_{filename}"


class BaseDocumentModel(BaseModelMixin, GeneralStatusFieldMixin, StrModelMixin):
	title = models.CharField(_("title"), max_length=70, null=False, blank=False)

	document_file = models.FileField(
		_("document file"),
		upload_to=saved_document_file_path,
		validators=[file_validator],
	)

	class Meta:
		abstract = True
		indexes = [
			models.Index(name="document_title_idx", fields=["title"]),
		]
