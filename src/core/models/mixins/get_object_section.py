from django.db import models


class GetObjectSectionMixin(models.Model):
    class Meta:
        abstract = True

    def get_object_section(self):
        if hasattr(self, "job"):
            return getattr(self, "job")
        elif hasattr(self, "client"):
            return getattr(self, "client")
        elif hasattr(self, "task"):
            return getattr(self, "task")
