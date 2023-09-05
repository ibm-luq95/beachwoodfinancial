# -*- coding: utf-8 -*-#
from django.db import models


class AccessProxyModelMixin(models.Model):
    class Meta:
        abstract = True

    def get_proxy_model(self):
        model = None
        model_name = self._meta.verbose_name
        match model_name:
            case "bookkeeper":
                from bookkeeper.models.bookkeeper_proxy import BookkeeperProxy

                model = BookkeeperProxy.objects.get(pk=self.pk)
            case "manager":
                from manager.models.manager_proxy import ManagerProxy

                model = ManagerProxy.objects.get(pk=self.pk)
            case "assistant":
                from assistant.models.assistant_proxy import AssistantProxy

                model = AssistantProxy.objects.get(pk=self.pk)
            case "job":
                from job.models.job_proxy import JobProxy

                model = JobProxy.objects.get(pk=self.pk)
            case "client":
                from client.models.client_proxy import ClientProxy

                model = ClientProxy.objects.get(pk=self.pk)
            case "task":
                from task.models.task_proxy import TaskProxy

                model = TaskProxy.objects.get(pk=self.pk)
        return model
