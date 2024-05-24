# -*- coding: utf-8 -*-#

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.edit import FormView

from beach_wood_user.forms import BWLoginForm
from beach_wood_user.models import BWUser
from core.cache import BWCacheViewMixin
from core.utils.developments.debugging_print_object import BWDebuggingPrint
from core.utils.grab_env_file import grab_env_file


class BWLoginViewBW(SuccessMessageMixin, BWCacheViewMixin, FormView):
    """
    BWLoginViewBW Default login form view

    Customized login form for staff members

    Args:
        SuccessMessageMixin (_type_): Django success message mixin
        BWCacheViewMixin (_type_): Backend cache mixin
        FormView (_type_): Django form view renderer

    """

    # http_method_names = ["post", "get"]
    # success_url = reverse_lazy("users:auth:login")
    template_name: str = "beach_wood_user/auth/login.html"
    form_class = BWLoginForm
    success_message: str = _("Login successfully")
    success_url = reverse_lazy("auth:login")

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        if self.request.GET.get("next"):
            self.request.session.setdefault("next", self.request.GET.get("next"))
        # check if user authenticated
        if self.request.user.is_authenticated:
            user_type = self.request.user.user_type  # type: ignore
            if user_type == "bookkeeper":
                return redirect("dashboard:bookkeeper:home")
            elif user_type == "manager" or user_type == "assistant":
                return redirect("dashboard:manager:home")

        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context.setdefault("title", _("Login"))

        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        config = grab_env_file()
        environment = config("STAGE_ENVIRONMENT", cast=str)
        if environment == "DEV" or environment == "STAGE" or environment == "LOCAL_DEV":
            kwargs.update({"initial": {"user_type": "manager"}})
        return kwargs

    # @watch_login()
    def form_valid(self, form):
        """
        This method is called when valid form data has been POSTED.
        It should return an HttpResponse.
        """
        try:
            # breakpoint()
            user_type = form.cleaned_data.get("user_type")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user_check = BWUser.objects.filter(email=email)  # type: ignore
            if not user_check:
                form.add_error("email", _("Email not exists!"))
                return self.form_invalid(form)
            #     # raise ValidationError(f"Email not exists!", code="invalid")
            user_check: BWUser | None = user_check.first()  # type: ignore
            check_user_type = user_check.user_type  # type: ignore
            #
            # check if the user type came from the form equal the user type saved in the db
            if user_type != check_user_type:
                form.add_error("user_type", _("User credentials not correct!!"))
                return self.form_invalid(form)
            user = authenticate(self.request, email=email, password=password)
            if user is not None:
                login(self.request, user)
            else:
                messages.error(self.request, _("User credentials not correct!"))
                return super().form_invalid(form)

            # Check if next url exists
            next_url = self.request.session.get("next", None)  # TODO: added to the end
            if next_url:
                return redirect(next_url)

            if check_user_type == "manager" or check_user_type == "assistant":
                self.success_url = reverse_lazy("dashboard:manager:home")
            elif check_user_type == "bookkeeper":
                self.success_url = reverse_lazy("dashboard:bookkeeper:home")

            return super().form_valid(form)
        except Exception:
            BWDebuggingPrint.get_console_obj().print_exception(show_locals=False)
            messages.error(self.request, _("Error while login"))
            return super().form_invalid(form)
