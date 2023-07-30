# -*- coding: utf-8 -*-#
from typing import Any

from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ImproperlyConfigured
from django.db import transaction
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _

from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    RedirectView,
    FormView,
)
from django.views.generic.detail import SingleObjectMixin

from beach_wood_user.models import BWUser
from bookkeeper.filters import BookkeeperFilter
from bookkeeper.forms import BookkeeperForm
from bookkeeper.models import BookkeeperProxy
from core.cache import BWCacheViewMixin
from core.constants import LIST_VIEW_PAGINATE_BY
from core.constants.users import CON_BOOKKEEPER
from core.utils import debugging_print
from core.views.mixins import (
    BWBaseListViewMixin,
    BWManagerAccessMixin,
    BWLoginRequiredMixin,
)


class BookkeeperListView(
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    ListView,
):
    # permission_required = "client.can_view_list"
    template_name = "bookkeeper/list.html"
    model = BookkeeperProxy
    paginate_by = LIST_VIEW_PAGINATE_BY
    list_type = "list"
    queryset = BookkeeperProxy.objects.get_queryset().order_by("-user__created_at")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["title"] = _("Bookkeepers")
        context.setdefault("filter_form", self.filterset.form)
        context.setdefault("list_type", self.list_type)
        context.setdefault("page_header", "notes".title())

        # debugging_print(self.filterset.form["name"])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = BookkeeperFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs


class BookkeeperCreateView(
    SuccessMessageMixin,
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
    BWCacheViewMixin,
    FormView,
):
    # permission_required = "client.add_client"
    template_name = "bookkeeper/create.html"
    form_class = BookkeeperForm
    success_message = _("Bookkeeper created successfully")
    success_url = reverse_lazy("dashboard:management_bookkeeper:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Create a new bookkeeper"))
        return context

    def form_valid(self, form: BookkeeperForm):
        """If the form is valid, save the associated model."""
        with transaction.atomic():
            user_details = {
                "first_name": form.cleaned_data.get("first_name"),
                "last_name": form.cleaned_data.get("last_name"),
                "email": form.cleaned_data.get("email"),
                "user_type": form.STAFF_MEMBER_TYPE,
            }
            new_user = BWUser.objects.create(**user_details)
            new_user.bookkeeper.profile_picture = form.cleaned_data.get("profile_picture")
            new_user.bookkeeper.bio = form.cleaned_data.get("bio")
            new_user.bookkeeper.save()
        return super().form_valid(form)

    # def get_initial(self) -> dict[str, Any]:
    #     return {"user_type": CON_BOOKKEEPER}


class BookkeeperDetailsView(
    BWLoginRequiredMixin, BWManagerAccessMixin, SuccessMessageMixin, DetailView
):
    template_name = "bookkeeper/details.html"
    model = BookkeeperProxy

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", f"{self.object.user.fullname}" + _("Bookkeeper"))
        return context


class BookkeeperUpdateView(
    SuccessMessageMixin,
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
    BWCacheViewMixin,
    SingleObjectMixin,
    FormView,
):
    # permission_required = "client.add_client"
    template_name = "bookkeeper/update.html"
    form_class = BookkeeperForm
    # success_message = _("Bookkeeper updated successfully")
    # success_url = reverse_lazy("dashboard:management_bookkeeper:list")
    model = BookkeeperProxy

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        self.object = self.get_object()  # this must be before super()
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Update bookkeeper"))
        return context

    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return _(f"Bookkeeper {self.object.user.fullname} updated successfully!")

    def get_object(self, queryset=None):
        """
        Retrieve the object that this view is displaying.
        """
        if queryset is None:
            queryset = self.get_queryset()
        # Retrieve the object

        return queryset.get(pk=self.kwargs["pk"])

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        success_url = reverse_lazy(
            "dashboard:management_bookkeeper:update", kwargs={"pk": self.object.pk}
        )
        return str(success_url)  # success_url may be lazy

    def get_initial(self) -> dict:
        initial = super().get_initial()
        initial["email"] = self.object.user.email
        initial["first_name"] = self.object.user.first_name
        initial["last_name"] = self.object.user.last_name
        initial["bio"] = self.object.bio
        initial["profile_picture"] = self.object.profile_picture

        return initial

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form: BookkeeperForm):
        """If the form is valid, save the associated model."""
        debugging_print("Form valid")
        with transaction.atomic():
            bookkeeper = self.object
            user_details = {
                "first_name": form.cleaned_data.get("first_name"),
                "last_name": form.cleaned_data.get("last_name"),
                "email": form.cleaned_data.get("email"),
                "user_type": form.STAFF_MEMBER_TYPE,
            }
            for key, value in user_details.items():
                setattr(bookkeeper.user, key, value)
            bookkeeper.user.save()
            bookkeeper.profile_picture = form.cleaned_data.get("profile_picture")
            bookkeeper.bio = form.cleaned_data.get("bio")
            bookkeeper.save()
        return super().form_valid(form)


class BookkeeperDeleteView(
    BWLoginRequiredMixin,
    BWManagerAccessMixin,
    BWCacheViewMixin,
    BWBaseListViewMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = "bookkeeper/delete.html"
    model = BookkeeperProxy
    success_message = _("Bookkeeper deleted successfully")
    success_url = reverse_lazy("dashboard:management_bookkeeper:list")

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Delete bookkeeper"))
        return context
