# -*- coding: utf-8 -*-#
from django.db.models import Q

from core.constants.status_labels import CON_COMPLETED, CON_ARCHIVED


class BWArchiveListViewMixin:
    """
    Mixin class that provides functionality for retrieving archived querysets.

    Methods:
        get_queryset() -> QuerySet: Retrieves the queryset for archived objects.

    """

    def get_queryset(self):
        """
        Retrieves the queryset for archived objects.

        Returns:
            QuerySet: The queryset filtered by completed or archived status.

        """
        queryset = self.model.objects.filter(Q(status__in=[CON_COMPLETED, CON_ARCHIVED]))
        return queryset
