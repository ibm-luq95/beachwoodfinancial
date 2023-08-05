# -*- coding: utf-8 -*-#
import traceback

from django.contrib.auth.models import Group, Permission
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _

from assistant.models import AssistantProxy
from beach_wood_user.models import Profile
from beach_wood_user.models.beach_wood_user import BWUser
from bookkeeper.models import BookkeeperProxy
from core.constants import BOOKKEEPER_GROUP_NAME, MANAGER_GROUP_NAME, ASSISTANT_GROUP_NAME
from core.utils import get_formatted_logger, debugging_print, colored_output_with_logging
from manager.models import ManagerProxy

# TODO: remove the custom logger before push (only for development)
# ###### [Custom Logger] #########
logger = get_formatted_logger()


# ###### [Custom Logger] #########


@receiver(post_save, sender=BWUser)
def assign_groups(sender, instance: BWUser, created: bool, **kwargs):
    try:
        if created:
            created_user = instance
            user_type = created_user.user_type

            with transaction.atomic():
                match user_type:
                    case "assistant":
                        group = ASSISTANT_GROUP_NAME
                        permission_codename = "assistant_user"
                        assistant = AssistantProxy.objects.create(
                            user=created_user, profile=Profile.objects.create()
                        )
                        # # Create profile for new user
                        # assistant.profile = Profile()
                        # assistant.save()
                    case "bookkeeper":
                        group = BOOKKEEPER_GROUP_NAME
                        permission_codename = "bookkeeper_user"
                        bookkeeper = BookkeeperProxy.objects.create(
                            user=created_user, profile=Profile.objects.create()
                        )
                        # # Create profile for new user
                        # bookkeeper.profile = Profile()
                        # bookkeeper.save()
                    case "manager":
                        group = MANAGER_GROUP_NAME
                        permission_codename = "manager_user"
                        manager = ManagerProxy.objects.create(
                            user=created_user, profile=Profile.objects.create()
                        )
                        # # Create profile for new user
                        # manager.profile = Profile()
                        # manager.save()
                # fetch user group
                group_object = Group.objects.filter(name=group)
                if not group_object:
                    # raise ProjectError("USER", message=f"The group {group} not exists!")
                    # raise Exception(_(f"The group {group} not exists!"))
                    colored_output_with_logging(
                        is_logged=True,
                        text=_(f"The group {group} not exists!"),
                        log_level="warning",
                        color="yellow",
                    )
                else:
                    group_object = group_object.first()
                    created_user.groups.add(group_object)

                # fetch user permissions
                permission_object = Permission.objects.filter(codename=permission_codename)
                if not permission_object:
                    colored_output_with_logging(
                        is_logged=True,
                        text=_(f"The permission {permission_codename} not exists!"),
                        log_level="warning",
                        color="yellow",
                    )
                else:
                    permission_object = permission_object.first()
                    created_user.user_permissions.add(permission_object)

                created_user.save()

    except Exception as ex:
        colored_output_with_logging(
            is_logged=True, text=traceback.format_exc(), log_level="error", color="red"
        )
        raise Exception(str(ex))
