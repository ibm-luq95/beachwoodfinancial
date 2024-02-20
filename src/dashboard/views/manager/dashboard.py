# -*- coding: utf-8 -*-#
from django.contrib import messages
from django.contrib.admin.models import LogEntry
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from core.cache import BWCacheViewMixin
from core.models import CRUDEventProxy
from core.utils import get_formatted_logger
from core.utils.developments.debugging_print_object import BWDebuggingPrint
from core.views.mixins import BWLoginRequiredMixin, BWManagerAccessMixin
from client.models import ClientProxy
from special_assignment.models import SpecialAssignmentProxy
from task.models import TaskProxy
from note.models import Note
from document.models import Document

logger = get_formatted_logger("bw_error_logger")


class DashboardViewBW(
    BWLoginRequiredMixin, BWManagerAccessMixin, BWCacheViewMixin, TemplateView
):
    template_name = "dashboard/manager/dashboard.html"
    http_method_names = ["get"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Manager dashboard"))
        messages.set_level(self.request, messages.DEBUG)
        clients = ClientProxy.objects.all().order_by("-created_at")[:5]
        documents_count = Document.objects.count()
        notes_count = Note.objects.count()
        tasks_count = TaskProxy.objects.count()

        last_activities = CRUDEventProxy.objects.all().order_by("-datetime")[:4]
        special_assignments = SpecialAssignmentProxy.objects.all().order_by("-created_at")[:4]
        context.setdefault("clients", clients)
        context.setdefault("documents_count", documents_count)
        context.setdefault("notes_count", notes_count)
        context.setdefault("tasks_count", tasks_count)
        context.setdefault("special_assignments", special_assignments)
        context.setdefault("last_activities", last_activities)

        return context
