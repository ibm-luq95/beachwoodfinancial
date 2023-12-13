from django.db import models
from django.utils.translation import gettext as _

from core.choices import TaskTypeEnum, TaskStatusEnum
from core.models.mixins import StrModelMixin, BaseModelMixin
from core.models.mixins.access_proxy_models_mixin import AccessProxyModelMixin
from core.models.mixins.cron_column_mixin import CronColumnMixin


class BaseTaskModel(BaseModelMixin, AccessProxyModelMixin, CronColumnMixin, StrModelMixin):
	title = models.CharField(_("title"), max_length=80, null=True)
	task_type = models.CharField(
		_("task type"),
		max_length=15,
		null=True,
		blank=True,
		choices=TaskTypeEnum.choices,
	)
	status = models.CharField(
		_("status"),
		max_length=15,
		null=True,
		blank=True,
		choices=TaskStatusEnum.choices,
		default=TaskStatusEnum.NOT_STARTED,
	)
	is_completed = models.BooleanField(
		_("is completed"), default=False, editable=False, db_index=True
	)
	hints = models.CharField(
		_("hints"),
		max_length=60,
		null=True,
		blank=True,
		help_text=_("Hints help to this task"),
	)
	additional_notes = models.TextField(
		_("additional notes"),
		null=True,
		blank=True,
		help_text=_("Additional note for the task"),
	)

	class Meta(BaseModelMixin.Meta):
		abstract = True
