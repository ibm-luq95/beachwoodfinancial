# -*- coding: utf-8 -*-#
import traceback

from core.constants.status_labels import CON_PAST_DUE, CON_STALLED, CON_NEED_INFO
from core.models.querysets import BaseQuerySetMixin
from bookkeeper.models import Bookkeeper
from core.utils import BeachWoodFinancialError, get_formatted_logger, debugging_print
from django.db.models import Q

logger = get_formatted_logger()


class BookkeeperProxy(Bookkeeper):
    class Meta(Bookkeeper.Meta):
        proxy = True
        permissions = [
            ("bookkeeper_user", "Bookkeeper User"),
            (
                "bookkeeper_can_delete_special_assignment",
                "Bookkeeper can delete special assignment",
            ),
        ]

    @property
    def get_bookkeeper(self) -> Bookkeeper:
        return Bookkeeper.objects.get(pk=self.pk)

    def get_tasks_count(self):
        all_tasks = []
        all_jobs = self.user.jobs.all()
        if all_jobs:
            for job in all_jobs:
                all_tasks.append(job.tasks.count())
        return sum(all_tasks)

    # def get_all_tasks_qs(self) -> BaseQuerySetMixin | None:
    #     from task.models import TaskProxy
    #
    #     bookkeeper_jobs = self.get_user_jobs()
    #     debugging_print(bookkeeper_jobs)
    #     if bookkeeper_jobs:
    #         all_tasks_list = []
    #         for job in bookkeeper_jobs:
    #             tasks = job.tasks.all()
    #             if tasks:
    #                 all_tasks_list = all_tasks_list + [task.pk for task in tasks]
    #         all_tasks_qs = TaskProxy.objects.filter(pk__in=all_tasks_list)
    #         return all_tasks_qs
    #     else:
    #         return None

    @property
    def get_clients_total(self) -> int:
        total_list = set()
        jobs = self.jobs.all()
        if jobs:
            for job in jobs:
                total_list.add(str(job.client.pk))
        return len(total_list)

    def get_tasks(self) -> list:
        all_lists = []
        all_jobs = self.user.jobs.all()
        if all_jobs:
            for job in all_jobs:
                tasks = job.tasks.all()
                if tasks:
                    for task in tasks:
                        all_lists.append(task)
        return all_lists

    def get_user_jobs(self) -> BaseQuerySetMixin | None:
        if hasattr(self.user, "jobs"):
            return self.user.jobs.all()
        else:
            return None

    def get_past_due_jobs(self) -> BaseQuerySetMixin | None:
        if hasattr(self.user, "jobs"):
            return self.user.jobs.filter(status=CON_PAST_DUE)
        else:
            return None

    def get_stats_jobs(self) -> BaseQuerySetMixin | None:
        if hasattr(self.user, "jobs"):
            return self.user.jobs.filter(Q(state=CON_STALLED) | Q(state=CON_NEED_INFO))
        else:
            return None

    def get_last_tasks(self, task_limit: int = 5) -> list:
        """Retrieve last tasks for bookkeeper

        Args:
            self: bookkeeper instance
            task_limit: int limit of last tasks
        Raises:
            ProjectError: If any exception occurred
            Exception: Any exception will occur will return None

        Returns:
            list: List of last tasks
            None: If any exception occurred
        """
        try:
            tasks_list = []
            all_jobs = self.get_user_jobs()
            all_jobs = all_jobs[:task_limit]
            if all_jobs:
                for job in all_jobs:
                    # debugging_print(job.title)
                    if job.tasks.filter():
                        for task in job.tasks.filter():
                            if len(tasks_list) <= task_limit:
                                tasks_list.append(task)
            # print(len(tasks_list))
            # print(type(tasks_list))
            return tasks_list
        except BeachWoodFinancialError as ex:
            logger.error(traceback.format_exc())
            raise Exception(ex.message)
        except Exception as ex:
            logger.error(traceback.format_exc())
            raise Exception(str(ex))
