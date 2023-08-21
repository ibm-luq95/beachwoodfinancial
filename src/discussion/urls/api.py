# -*- coding: utf-8 -*-#
from rest_framework import routers

from discussion.views import DiscussionViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"discussion-api", DiscussionViewSet, basename="discussion-api-router")

urlpatterns = router.urls
