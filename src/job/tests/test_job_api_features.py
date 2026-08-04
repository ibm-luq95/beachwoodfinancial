# -*- coding: utf-8 -*-#
from __future__ import annotations

import pytest
from client.views.api import ClientViewSet
from discussion.views.api import DiscussionViewSet
from job.views.api import JobViewSet
from task.views.api import TaskViewSet


@pytest.mark.django_db
def test_core_viewsets_have_filter_search_ordering() -> None:
    for viewset_cls in [JobViewSet, TaskViewSet, ClientViewSet, DiscussionViewSet]:
        assert hasattr(viewset_cls, "filterset_fields") and len(viewset_cls.filterset_fields) > 0
        assert hasattr(viewset_cls, "search_fields") and len(viewset_cls.search_fields) > 0
        assert hasattr(viewset_cls, "ordering_fields") and len(viewset_cls.ordering_fields) > 0
