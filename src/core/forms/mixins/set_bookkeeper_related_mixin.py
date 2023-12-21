# -*- coding: utf-8 -*-#


class InitBookkeeperRelatedFieldsMixin:
    def __init__(self, bookkeeper=None, *args, **kwargs):
        if "client" in self.fields:
            self.fields["client"].queryset = self.fields["client"].queryset.order_by(
                "name"
            )
        if "job" in self.fields:
            self.fields["job"].queryset = self.fields["job"].queryset.order_by("title")
        if "task" in self.fields:
            self.fields["task"].queryset = self.fields["task"].queryset.order_by("title")
        if bookkeeper is not None:
            if self.fields.get("client") is not None:
                self.fields["client"].queryset = bookkeeper.get_proxy_model().clients.all()
            if self.fields.get("job") is not None:
                self.fields["job"].queryset = bookkeeper.get_proxy_model().get_user_jobs()
            if self.fields.get("task") is not None:
                self.fields[
                    "task"
                ].queryset = bookkeeper.get_proxy_model().get_all_related_items("tasks")
