# -*- coding: utf-8 -*-#
from django.db import transaction
from django.db.models import Q

from bookkeeper.models import BookkeeperProxy
from core.constants.status_labels import (
	CON_ARCHIVED,
	CON_COMPLETED,
	CON_ENABLED,
)
from job.models import Job


class JobProxy(Job):
	class Meta(Job.Meta):
		proxy = True

	def unplug_bookkeeper_for_client_finished_job(self):
		managed_by = self.managed_by
		if self.status == CON_COMPLETED or self.status == CON_ARCHIVED:
			if managed_by:
				with transaction.atomic():
					client = self.client
					if hasattr(managed_by, "bookkeeper"):
						bookkeeper_obj = managed_by.bookkeeper
						# debugging_print(bookkeeper_obj)
						bookkeeper_obj = BookkeeperProxy.objects.get(pk=bookkeeper_obj.pk)
						client.bookkeepers.remove(bookkeeper_obj)
						client.save()
						# debugging_print(self.model_class())
						JobProxy.objects.filter(pk=self.pk).update(managed_by=None)

	def archive_and_unarchived_related_items(self, status: str) -> None:
		with transaction.atomic():
			documents = self.documents.all()
			tasks = self.tasks.all()
			notes = self.notes.all()
			if status == CON_ARCHIVED or status == CON_COMPLETED:
				# Set notes to archived
				if notes:
					notes.update(status=CON_ARCHIVED)
				# Set documents to archived
				if documents:
					documents.update(status=CON_ARCHIVED)
				# Set tasks to archived
				if tasks:
					# tasks.update(status=CON_ARCHIVED)
					for task in tasks:
						task.status = (
							CON_ARCHIVED if status == CON_ARCHIVED else CON_COMPLETED
						)
						# task.status = CON_ARCHIVED
						task.save()
			else:
				# Set notes to enabled
				if notes:
					notes.filter(Q(status=CON_ARCHIVED)).update(status=CON_ENABLED)
				# Set documents to enabled
				if documents:
					documents.filter(Q(status=CON_ARCHIVED)).update(status=CON_ENABLED)
				# Set tasks to archived
				if tasks:
					with transaction.atomic():
						# tasks.filter(Q(status=CON_ARCHIVED)).update(status=CON_NOT_STARTED)
						tasks = tasks.filter()
						for task in tasks:
							logged_task = task.history.filter()
							if logged_task.exists():
								logged_task = logged_task.first()
								task.status = logged_task.previous_status
								task.save()
								logged_task.delete()
