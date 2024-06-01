# -*- coding: utf-8 -*-#
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import update_last_login

from core.utils.developments.debugging_print_object import BWDebuggingPrint


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    # if user.user_type == "manager":
    user.last_login = timezone.now()
    # user.save(update_fields=["last_login"])
    user.save()
    BWDebuggingPrint.pprint("Update last login done")


user_logged_in.disconnect(update_last_login, dispatch_uid="update_last_login")
user_logged_in.disconnect(user_logged_in, dispatch_uid="user_logged_in")
# user_logged_in.disconnect(
#     update_last_login, sender=settings.AUTH_USER_MODEL, dispatch_uid="update_last_login"
# )
