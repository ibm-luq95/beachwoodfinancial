from django import forms

from core.forms import (
    BaseModelFormMixin,
    JoditFormMixin,
)
from task.models import TaskProxy


class TaskForm(BaseModelFormMixin, JoditFormMixin):
    field_order = [
        "title",
        "job",
        "task_type",
        "status",
        "start_date",
        "due_date",
        "additional_notes",
        "hints",
    ]

    # additional_notes = SummernoteTextFormField(required=False)

    def __init__(
        self,
        client=None,
        is_disable_job=False,
        job=None,
        remove_type_and_status=False,
        remove_job=False,
        add_jodit_css_class=False,
        *args,
        **kwargs,
    ):
        super(TaskForm, self).__init__(*args, **kwargs)
        JoditFormMixin.__init__(self, add_jodit_css_class=add_jodit_css_class)
        self.fields["job"].widget.attrs.update({"class": "input"})

        # check if job passed and set it to job input
        if job is not None:
            self.fields["job"].initial = job

        # this used when update task in bookkeeper dashboard
        if is_disable_job is True:
            self.fields.pop("job")

        # this used in manager client details view, to pass only jobs for custom client
        if self.initial.get("client", None) is not None:
            self.fields["job"].queryset = Job.objects.filter(
                client=self.initial.get("client")
            )
            # self.fields["client"].widget.attrs.update({"class": "cursor-not-allowed readonly-select"})

        if remove_type_and_status is True:
            # self.fields.pop("status")
            self.fields.pop("task_type")
            self.fields.pop("hints")

        if remove_job is True:
            self.fields.pop("job")

    class Meta(BaseModelFormMixin.Meta):
        model = TaskProxy
        # widgets = {
        #     "additional_notes": forms.TextInput()
        # }
