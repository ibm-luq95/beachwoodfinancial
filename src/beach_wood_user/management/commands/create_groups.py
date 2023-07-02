# -*- coding: utf-8 -*-#

from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.translation import gettext as _

from core.constants import BOOKKEEPER_GROUP_NAME, MANAGER_GROUP_NAME, ASSISTANT_GROUP_NAME
from core.management.mixins import CommandStdOutputMixin


# from core.utils import debugging_print


class Command(BaseCommand, CommandStdOutputMixin):
    help = _("Create groups for manager, bookkeeper, assistant")
    apps_name = ("manager", "bookkeeper", "assistant")
    groups_names = (BOOKKEEPER_GROUP_NAME, ASSISTANT_GROUP_NAME, MANAGER_GROUP_NAME)

    def add_arguments(self, parser):
        parser.add_argument(
            "-a",
            "--app-name",
            type=str,
            help=_("Pass app specific name to create group only"),
            required=False,
        )
        parser.add_argument(
            "--clear-all-groups",
            "-ca",
            nargs="?",
            action="store",
            const=True,
            type=str,
            required=False,
            help=_("Delete all groups for manager, bookkeeper, assistant"),
            # default=False,
        )

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                passed_app = options.get("app_name")
                passed_clear = options.get("clear_all_groups")
                # debugging_print(options)
                # debugging_print(passed_clear)
                if passed_clear:
                    self.clear_groups()
                    return
                if passed_app:
                    if passed_app not in self.apps_name:
                        raise Exception(
                            _(
                                f"The app {passed_app} not allowed!, the allowed {self.apps_name}"
                            )
                        )
                    models = [passed_app]
                else:
                    models = ["manager", "bookkeeper", "assistant"]

                for model in models:
                    # content_type = ContentType.objects.get_for_model(Bookkeeper)
                    permission = Permission.objects.filter(
                        content_type__app_label=model
                    ).values_list("codename", flat=True)
                    permissions = list(permission)
                    # debugging_print(permission)
                    group_obj = None
                    match model:
                        case "bookkeeper":
                            group_obj = Group.objects.create(name=BOOKKEEPER_GROUP_NAME)
                        case "assistant":
                            group_obj = Group.objects.create(name=ASSISTANT_GROUP_NAME)
                        case "manager":
                            group_obj = Group.objects.create(name=MANAGER_GROUP_NAME)
                        case _:
                            raise Exception(_(f"The {model} not exists!"))
                    # for perm in permissions:
                    #     pe = Permission.objects.filter(codename=perm)
                    #     if pe:
                    #         pe = pe.first()
                    #         group_obj.permissions.add(pe)
                    #         group_obj.save()
                    #     else:
                    #         self.stdout_output("error", f"Permission {perm} not exists!")
                    # debugging_print(group_obj.permissions.all())
                    self.stdout_output(
                        "success", _(f"Group {group_obj.name} created successfully")
                    )
        except Exception as ex:
            self.stdout_output("error", str(ex))

    def clear_groups(self):
        try:
            with transaction.atomic():
                for group in self.groups_names:
                    group_obj = Group.objects.filter(name=group)
                    if group_obj.count() <= 0:
                        self.stdout_output("error", _(f"Group {group} not exists!"))
                        pass
                    else:
                        group_obj = group_obj.first()
                        self.stdout_output("warn", _(f"Deleting {group}"))
                        group_obj.delete()

        except Exception as ex:
            self.stdout_output("error", str(ex))
