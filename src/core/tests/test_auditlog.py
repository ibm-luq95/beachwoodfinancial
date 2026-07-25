from __future__ import annotations

import pytest
from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.management import call_command

from auditlog.models import LogEntry
from auditlog.registry import auditlog
from core.models import LogEntryProxy


@pytest.mark.django_db
def test_core_models_are_registered() -> None:
    # Verify concrete models
    assert auditlog.contains(apps.get_model("beach_wood_user", "BWUser"))
    assert auditlog.contains(apps.get_model("client", "Client"))
    assert auditlog.contains(apps.get_model("job", "Job"))
    assert auditlog.contains(apps.get_model("task", "Task"))
    assert auditlog.contains(apps.get_model("document", "Document"))
    assert auditlog.contains(apps.get_model("note", "Note"))
    assert auditlog.contains(apps.get_model("special_assignment", "SpecialAssignment"))

    # Verify proxy models
    assert auditlog.contains(apps.get_model("client", "ClientProxy"))
    assert auditlog.contains(apps.get_model("job", "JobProxy"))
    assert auditlog.contains(apps.get_model("task", "TaskProxy"))
    assert auditlog.contains(apps.get_model("special_assignment", "SpecialAssignmentProxy"))
    assert auditlog.contains(apps.get_model("assistant", "AssistantProxy"))
    assert auditlog.contains(apps.get_model("bookkeeper", "BookkeeperProxy"))
    assert auditlog.contains(apps.get_model("manager", "ManagerProxy"))


@pytest.mark.django_db
def test_log_entry_proxy_properties() -> None:
    User = get_user_model()
    user = User.objects.create_user(
        email="test_audit_user@example.com",
        password="test_password"
    )
    
    ContentType = apps.get_model("contenttypes", "ContentType")
    content_type = ContentType.objects.get_for_model(user)

    entry = LogEntry.objects.create(
        content_type=content_type,
        object_pk=str(user.pk),
        object_repr=str(user),
        action=LogEntry.Action.CREATE,
        actor=user,
        changes={"email": ["None", "test_audit_user@example.com"]}
    )
    proxy = LogEntryProxy.objects.get(pk=entry.pk)
    
    assert proxy.datetime == proxy.timestamp
    assert proxy.user == user
    assert proxy.get_event_type_display() == "Create"


@pytest.mark.django_db
def test_log_entry_proxy_soft_delete_and_update() -> None:
    User = get_user_model()
    user = User.objects.create_user(
        email="test_audit_user_2@example.com",
        password="test_password"
    )
    ContentType = apps.get_model("contenttypes", "ContentType")
    content_type = ContentType.objects.get_for_model(user)

    entry_delete = LogEntry.objects.create(
        content_type=content_type,
        object_pk=str(user.pk),
        object_repr=str(user),
        action=LogEntry.Action.UPDATE,
        changes={"is_deleted": [False, True]}
    )
    proxy_delete = LogEntryProxy.objects.get(pk=entry_delete.pk)
    assert proxy_delete.is_custom_deleted is True
    assert proxy_delete.is_custom_update is False

    entry_update = LogEntry.objects.create(
        content_type=content_type,
        object_pk=str(user.pk),
        object_repr=str(user),
        action=LogEntry.Action.UPDATE,
        changes={"email": ["old@example.com", "new@example.com"]}
    )
    proxy_update = LogEntryProxy.objects.get(pk=entry_update.pk)
    assert proxy_update.is_custom_deleted is False
    assert proxy_update.is_custom_update is True


@pytest.mark.django_db
def test_backfill_command_execution() -> None:
    call_command("backfill_audit_logs")
