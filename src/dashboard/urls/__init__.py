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
    path(
        "client-category/",
        include("client_category.urls"),
        name="client-category",
    ),
    path(
        "important-contact/",
        include("important_contact.urls"),
        name="important-contact",
    ),
    path(
        "client-account/",
        include("client_account.urls"),
        name="client-account",
    ),
    path(
        "client/",
        include("client.urls"),
        name="client",
    ),
    path(
        "note/",
        include("note.urls"),
        name="note",
    ),
]
