from django.urls import path, include

from task.views import TaskListView, TaskUpdateView, TaskCreateView, TaskDeleteView

app_name = "task"

urlpatterns = [
    path("", TaskListView.as_view(), name="list"),
    path("create", TaskCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", TaskUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", TaskDeleteView.as_view(), name="delete"),
]
