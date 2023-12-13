from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from core.cache import BWCacheViewMixin

from core.constants import LIST_VIEW_PAGINATE_BY

from core.views.mixins import BWLoginRequiredMixin, BWBaseListViewMixin
from job_template.models import JobTemplate


class JobTemplateListView(
    PermissionRequiredMixin,
    BWLoginRequiredMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    permission_required = "job.can_view_list"

    permission_denied_message = _("You do not have permission to access this page.")
    template_name = "job_template/list.html"
    model = JobTemplate

    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "list"
