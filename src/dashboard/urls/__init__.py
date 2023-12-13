# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "dashboard"

urlpatterns = [
    path("manager/", include("dashboard.urls.manager"), name="dashboard-manager-urls"),
    path(
        "bookkeeper/",
        include("dashboard.urls.bookkeeper"),
        name="dashboard-bookkeeper-urls",
    ),
    path("client-category/", include("client_category.urls"), name="client-category"),
    path(
        "important-contact/", include("important_contact.urls"), name="important-contact"
    ),
    path("client-account/", include("client_account.urls"), name="client-account"),
    path("client/", include("client.urls"), name="client"),
    path("note/", include("note.urls"), name="note"),
    path("document/", include("document.urls"), name="document"),
    path("job-category/", include("job_category.urls"), name="job_category"),
    path("task/", include("task.urls"), name="task"),
    path("job/", include("job.urls"), name="job"),
    path("site-settings/", include("site_settings.urls"), name="site_settings"),
    path("assignments/", include("special_assignment.urls"), name="special_assignment"),
    path("discussions/", include("discussion.urls"), name="discussions"),
    path(
        "management/bookkeeper/", include("bookkeeper.urls"), name="management_bookkeepers"
    ),
    path("management/assistant/", include("assistant.urls"), name="management_assistants"),
    path("management/manager/", include("manager.urls"), name="management_managers"),
    path("reports/", include("reports.urls"), name="reports"),
    path("staff/", include("beach_wood_user.urls.staff"), name="staff"),
    path("job-templates/", include("job_template.urls"), name="job_template"),
]
