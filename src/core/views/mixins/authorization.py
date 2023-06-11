# -*- coding: utf-8 -*-#
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied


class BWManagerAccessMixin(PermissionRequiredMixin):
    permission_required = ["manager.manager_user"]

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect_to_login(
                self.request.get_full_path(),
                self.get_login_url(),
                self.get_redirect_field_name(),
            )

        if not self.has_permission():
            raise PermissionDenied

        return super(BWManagerAccessMixin, self).dispatch(request, *args, **kwargs)


class BWManagerAssistantAccessMixin(UserPassesTestMixin):
    # permission_required = ("manager.manager_user", "assistant.assistant_user")

    # def has_permission(self) -> bool:
    #     # perms = self.get_permission_required()
    #     # print(self.request.user.has_perms(perms))
    #     # return self.request.user.has_perms(perms)
    #     user_type = self.request.user.user_type
    #     return user_type == "manager" or user_type == "assistant"

    def test_func(self) -> bool | None:
        user_type = self.request.user.user_type
        return (
            user_type == "manager" or user_type == "assistant" or user_type == "bookkeeper"
        )
