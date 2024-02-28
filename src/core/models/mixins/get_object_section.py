from django.db import models


class GetObjectSectionMixin(models.Model):
    class Meta:
        abstract = True

    def get_object_section(self):
        """
        Method to get the object section based on the presence of 'job', 'client',
         or 'task' attributes.
        """
        if hasattr(self, "job"):
            return getattr(self, "job")
        elif hasattr(self, "client"):
            return getattr(self, "client")
        elif hasattr(self, "task"):
            return getattr(self, "task")

    @property
    def get_related_objects_as_dict(self) -> dict:
        data = {"job": None, "client": None, "task": None}
        if hasattr(self, "job"):
            data.update({"job": getattr(self, "job")})
        if hasattr(self, "client"):
            data.update({"client": getattr(self, "client")})
        if hasattr(self, "task"):
            data.update({"task": getattr(self, "task")})

        return data

    @property
    def get_multiple_sections(self) -> dict:
        return {
            "task": self.get_object_section(),
            "job": self.get_object_section(),
            "client": self.get_object_section(),
        }
