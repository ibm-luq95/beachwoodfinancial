from typing import Any

from django.forms import ValidationError
from django.utils.translation import gettext as _

from core.forms import BaseModelFormMixin
from job_category.models import JobCategory


class JobCategoryForm(BaseModelFormMixin):
    def __int__(self, *args, **kwargs):
        super(JobCategoryForm, self).__init__(*args, **kwargs)

    def clean(self) -> dict[str, Any] | None:
        cleaned_data = super().clean()
        check = JobCategory.original_objects.filter(name=cleaned_data.get("name"))
        if check.exists():
            # self.add_error("name", cleaned_data.get('name'))
            raise ValidationError(
                _(f"The name: {cleaned_data.get('name')} exists!"), code="invalid"
            )
        return cleaned_data

    class Meta:
        model = JobCategory
        fields = ["name"]
