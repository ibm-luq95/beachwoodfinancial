from django.db import models


from task.models.base_abstract_task import BaseTaskModel
from django.db import models

from task_item.models import TaskItem


class TaskTemplate(BaseTaskModel):
	items = models.ManyToManyField(to=TaskItem, related_name="tasks")

	class Meta(BaseTaskModel.Meta):
		indexes = [
			models.Index(name="task_title_idx", fields=["title"]),
			models.Index(name="task_status_idx", fields=["status"]),
			models.Index(name="task_type_idx", fields=["task_type"]),
			models.Index(name="task_is_completed_idx", fields=["is_completed"]),
			models.Index(name="task_hints_idx", fields=["hints"]),
			models.Index(name="task_additional_notes_idx", fields=["additional_notes"]),
		]
