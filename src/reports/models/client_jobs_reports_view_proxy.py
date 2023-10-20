# -*- coding: utf-8 -*-#
from reports.models import ClientJobsReportsDBView


class ClientJobsReportsDBViewProxy(ClientJobsReportsDBView):
    class Meta:
        proxy = True
        managed = False
