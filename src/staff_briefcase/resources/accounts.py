# -*- coding: utf-8 -*-#
from import_export import resources

from staff_briefcase.models import StaffAccounts


class StaffAccountsResource(resources.ModelResource):
    class Meta:
        model = StaffAccounts
