from django.db.models import Q

from core.models.managers import SoftDeleteManager
from core.models.querysets import BaseQuerySetMixin
from core.constants.status_labels import CON_COMPLETED, CON_ARCHIVED


class TaskManager(SoftDeleteManager):
    def all(self) -> BaseQuerySetMixin:
        qs = self.get_queryset()
        field_names = [field.name for field in self.model._meta.fields]
        if "status" in field_names:
            qs = qs.filter(~Q(status__in=[CON_ARCHIVED]))
        return qs
