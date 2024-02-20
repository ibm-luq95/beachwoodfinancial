# -*- coding: utf-8 -*-#
import itertools
from django.contrib.auth.models import Permission

from django.contrib.contenttypes.models import ContentType

from core.constants.users import DEFAULT_PERMISSIONS_NEW_STAFF_MEMBER
from core.models.querysets import BaseQuerySetMixin


class PermissionHelper:
	@classmethod
	def get_bw_default_permissions(
		cls, as_list: bool = False, as_qs: bool = False, as_form_choices: bool = False
	) -> list | BaseQuerySetMixin:
		permissions_codename_list_objs = []
		for content_type_item in DEFAULT_PERMISSIONS_NEW_STAFF_MEMBER:
			content_type_object = ContentType.objects.get(
				app_label=content_type_item["app_label"],
				model=content_type_item["model_label"],
			)
			# BWDebuggingPrint.pprint(content_type_object)
			permissions_codename_labels = content_type_item.get(
				"permissions_codename_labels"
			)
			extra_permissions = content_type_item.get("extra_permissions", {})
			# BWDebuggingPrint.pprint(permissions_codename_labels)
			# BWDebuggingPrint.pprint(content_type_item)
			# BWDebuggingPrint.pprint(extra_permissions)
			extra_permissions_codename_labels = []
			if bool(extra_permissions):
				# the dict not empty
				extra_permissions_codename_labels = extra_permissions.get(
					"codename_labels"
				)
			for codename, extra_codename in itertools.zip_longest(
				permissions_codename_labels, extra_permissions_codename_labels
			):
				# BWDebuggingPrint.pprint(codename)
				# BWDebuggingPrint.pprint(extra_codename)
				if extra_codename:
					permission_object = Permission.objects.get(
						codename=extra_codename, content_type=content_type_object
					)
				else:
					permission_object = Permission.objects.get(
						codename=codename, content_type=content_type_object
					)
				permissions_codename_list_objs.append(permission_object)

		if as_list:
			return permissions_codename_list_objs
		elif as_qs:
			permissions_pks = [p.pk for p in permissions_codename_list_objs]
			permissions = Permission.objects.filter(pk__in=permissions_pks)
			return permissions
		elif as_form_choices:
			form_choices = []
			for permission in permissions_codename_list_objs:
				form_choices.append((
					permission.pk,
					permission,
					# (
					#     _(f"Critical option")
					#     if permission.codename in extra_permissions_codename_labels
					#     else ""
					# ),
				))
			# debugging_print(form_choices)
			return form_choices
