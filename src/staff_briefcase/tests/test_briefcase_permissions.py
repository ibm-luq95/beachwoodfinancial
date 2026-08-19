"""Unit tests for staff briefcase isolation and API role scoping."""
from __future__ import annotations

import pytest
from django.core.management import call_command
from django.test import RequestFactory
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from beach_wood_user.models import BWUser
from bookkeeper.models import BookkeeperProxy
from cfo.models import CFOProxy
from client.models import ClientProxy
from client.views.api import ClientDropdownView, ClientViewSet
from core.constants.users import (
    CON_BOOKKEEPER,
    CON_CFO,
    CON_MANAGER,
)
from staff_briefcase.models import StaffBriefcase, StaffDocuments, StaffNotes
from staff_briefcase.views.briefcase import (
    StaffBriefcaseDetailView,
    StaffBriefcaseListView,
)
from staff_briefcase.views.documents.api import StaffDocumentsViewSet
from staff_briefcase.views.notes.api import StaffNotesViewSet


@pytest.fixture(autouse=True)
def setup_groups(db: None) -> None:
    """Ensure Django auth groups exist."""
    call_command("create_groups")


@pytest.mark.django_db
class TestStaffBriefcasePermissions:
    """Test suite verifying briefcase isolation and API role boundaries."""

    def test_briefcase_list_and_details_isolation(self, rf: RequestFactory) -> None:
        """Verify staff members can only access their own briefcase."""
        manager = BWUser.objects.create_user(
            email="mgr_bc@example.com",
            password="ValidPassword123!",
            user_type=CON_MANAGER,
        )
        staff1 = BWUser.objects.create_user(
            email="staff1@example.com",
            password="ValidPassword123!",
            user_type=CON_BOOKKEEPER,
        )
        staff2 = BWUser.objects.create_user(
            email="staff2@example.com",
            password="ValidPassword123!",
            user_type=CON_BOOKKEEPER,
        )

        bc1 = StaffBriefcase.objects.get(user=staff1)
        bc2 = StaffBriefcase.objects.get(user=staff2)

        # ListView scoping
        list_view = StaffBriefcaseListView()
        req1 = rf.get("/briefcase/")
        req1.user = staff1
        list_view.request = req1
        staff1_qs = list_view.get_queryset()
        assert bc1 in staff1_qs
        assert bc2 not in staff1_qs

        # DetailView object permission
        detail_view = StaffBriefcaseDetailView()
        detail_view.kwargs = {"pk": bc2.pk}
        detail_view.object = bc2

        # Staff 1 trying to access Staff 2 briefcase
        detail_view.request = req1
        assert detail_view.test_func() is False

        # Staff 2 accessing own briefcase
        req2 = rf.get(f"/briefcase/{bc2.pk}/")
        req2.user = staff2
        detail_view.request = req2
        assert detail_view.test_func() is True

        # Manager accessing Staff 2 briefcase
        req_mgr = rf.get(f"/briefcase/{bc2.pk}/")
        req_mgr.user = manager
        detail_view.request = req_mgr
        assert detail_view.test_func() is True

    def test_staff_documents_and_notes_api_scoping(self) -> None:
        """Verify API ViewSets scope documents and notes per briefcase owner."""
        staff1 = BWUser.objects.create_user(
            email="staff_api1@example.com",
            password="ValidPassword123!",
            user_type=CON_BOOKKEEPER,
        )
        staff2 = BWUser.objects.create_user(
            email="staff_api2@example.com",
            password="ValidPassword123!",
            user_type=CON_BOOKKEEPER,
        )

        bc1 = StaffBriefcase.objects.get(user=staff1)
        bc2 = StaffBriefcase.objects.get(user=staff2)

        doc1 = StaffDocuments.objects.create(
            title="Doc Staff 1",
            document_file="staff_documents/test1.pdf",
        )
        bc1.documents.add(doc1)

        doc2 = StaffDocuments.objects.create(
            title="Doc Staff 2",
            document_file="staff_documents/test2.pdf",
        )
        bc2.documents.add(doc2)

        note1 = StaffNotes.objects.create(
            title="Note Staff 1",
            note="Confidential note 1",
        )
        bc1.notes.add(note1)

        note2 = StaffNotes.objects.create(
            title="Note Staff 2",
            note="Confidential note 2",
        )
        bc2.notes.add(note2)

        api_rf = APIRequestFactory()

        # Documents ViewSet for Staff 1
        doc_view = StaffDocumentsViewSet.as_view({"get": "list"})
        req_doc = api_rf.get("/staff_briefcase/api/documents-api/")
        force_authenticate(req_doc, user=staff1)
        res_doc = doc_view(req_doc)
        assert (
            res_doc.status_code == status.HTTP_200_OK
        ), f"Doc error: {res_doc.data if hasattr(res_doc, 'data') else res_doc.content}"
        doc_titles = [d["title"] for d in res_doc.data["results"]]
        assert "Doc Staff 1" in doc_titles
        assert "Doc Staff 2" not in doc_titles

        # Notes ViewSet for Staff 1
        note_view = StaffNotesViewSet.as_view({"get": "list"})
        req_note = api_rf.get("/staff_briefcase/api/notes-api/")
        force_authenticate(req_note, user=staff1)
        res_note = note_view(req_note)
        assert res_note.status_code == status.HTTP_200_OK
        note_titles = [n["title"] for n in res_note.data["results"]]
        assert "Note Staff 1" in note_titles
        assert "Note Staff 2" not in note_titles

    def test_client_api_assign_staff_permission(self) -> None:
        """Verify non-managers cannot assign staff to clients via API."""
        manager = BWUser.objects.create_user(
            email="mgr_assign@example.com",
            password="ValidPassword123!",
            user_type=CON_MANAGER,
        )
        bk = BWUser.objects.create_user(
            email="bk_assign@example.com",
            password="ValidPassword123!",
            user_type=CON_BOOKKEEPER,
        )
        client = ClientProxy.objects.create(name="Assign Test Client")

        api_rf = APIRequestFactory()
        assign_view = ClientViewSet.as_view({"post": "assign_bookkeeper"})

        # Bookkeeper attempting assignment -> 403 Forbidden
        req_bk = api_rf.post(
            "/client/api/client-api/assign_bookkeeper/",
            {"client": str(client.pk), "bookkeepers": [str(bk.bookkeeper.pk)]},
            format="json",
        )
        force_authenticate(req_bk, user=bk)
        res_bk = assign_view(req_bk)
        assert res_bk.status_code == status.HTTP_403_FORBIDDEN

        # Manager attempting assignment -> 200 OK
        req_mgr = api_rf.post(
            "/client/api/client-api/assign_bookkeeper/",
            {"client": str(client.pk), "bookkeepers": [str(bk.bookkeeper.pk)]},
            format="json",
        )
        force_authenticate(req_mgr, user=manager)
        res_mgr = assign_view(req_mgr)
        assert res_mgr.status_code == status.HTTP_200_OK, f"Error: {res_mgr.data}"
        client.refresh_from_db()
        assert bk.bookkeeper.get_proxy_model() in client.bookkeepers.all()

