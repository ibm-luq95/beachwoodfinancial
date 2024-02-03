# -*- coding: utf-8 -*-#
from typing import Optional

from django import forms
from django.utils.translation import gettext as _

from core.forms.mixins.remove_fields_mixin import RemoveFieldsMixin
from core.forms.widgets import RichHTMLEditorWidget, BWPasswordInputWidget


class AbstractStaffMemberForm(forms.Form, RemoveFieldsMixin):
	def __init__(
		self, user_type: str, removed_fields: Optional[list] = None, *args, **kwargs
	):
		super().__init__(*args, **kwargs)
		RemoveFieldsMixin.__init__(self, removed_fields=removed_fields)
		self.fields.get("user_type").initial = user_type
		if self.fields.get("password"):
			self.fields.get("password").widget.attrs["data-block-section"] = "user"
		if self.fields.get("confirm_password"):
			self.fields.get("confirm_password").widget.attrs["data-block-section"] = "user"
		self.fields.get("user_type").widget.attrs["data-block-section"] = "user"
		self.fields.get("email").widget.attrs["data-block-section"] = "user"
		self.fields.get("first_name").widget.attrs["data-block-section"] = "user"
		self.fields.get("last_name").widget.attrs["data-block-section"] = "user"
		self.fields.get("user_type").widget.attrs["data-block-section"] = "user"
		if self.fields.get("profile_picture"):
			self.fields.get("profile_picture").widget.attrs["data-block-section"] = (
				"profile"
			)
		self.fields.get("facebook").widget.attrs["data-block-section"] = "profile"
		self.fields.get("twitter").widget.attrs["data-block-section"] = "profile"
		self.fields.get("github").widget.attrs["data-block-section"] = "profile"
		self.fields.get("linkedin").widget.attrs["data-block-section"] = "profile"
		self.fields.get("instagram").widget.attrs["data-block-section"] = "profile"

	field_order = [
		"first_name",
		"last_name",
		"email",
		"password",
		"confirm_password",
		"profile_picture",
	]
	password = forms.CharField(
		label=_("Password"), required=False, widget=BWPasswordInputWidget
	)
	confirm_password = forms.CharField(
		label=_("Confirm Password"), required=False, widget=BWPasswordInputWidget
	)
	email = forms.EmailField(label=_("Email Address"), required=True)
	first_name = forms.CharField(label=_("First Name"), required=True)
	last_name = forms.CharField(label=_("Last Name"), required=True)
	profile_picture = forms.ImageField(label=_("Profile Picture"), required=False)
	address = forms.CharField(label=_("Address"), required=False)
	phone_number = forms.CharField(label=_("Phone number"), required=False)
	bio = forms.CharField(label=_("BIO"), widget=RichHTMLEditorWidget, required=False)
	user_type = forms.CharField(label="", widget=forms.HiddenInput, required=False)
	facebook = forms.URLField(label=_("Facebook"), required=False)
	twitter = forms.URLField(label=_("Twitter"), required=False)
	github = forms.URLField(label=_("Github"), required=False)
	linkedin = forms.URLField(label=_("Linkedin"), required=False)
	instagram = forms.URLField(label=_("Instagram"), required=False)

	class Meta:
		abstract = True

	def clean_confirm_password(self):
		password = self.cleaned_data.get("password")
		confirm_password = self.cleaned_data.get("confirm_password")
		if password != confirm_password:
			raise forms.ValidationError(
				_("Password confirmation not match!"), code="invalid"
			)
		return confirm_password

	def split_user_profiles_inputs(self, excluded_fields: Optional[list] = []) -> dict:
		inputs = dict()
		inputs["user"] = dict()
		inputs["profile"] = dict()
		for field_name, field in self.fields.items():
			# debugging_print(dir(field.bound_data()))
			if field_name not in excluded_fields:
				if field.widget.attrs.get("data-block-section") == "user":
					inputs["user"][field_name] = self.cleaned_data.get(field_name)
				elif field.widget.attrs.get("data-block-section") == "profile":
					inputs["profile"][field_name] = self.cleaned_data.get(field_name)

		# debugging_print(inputs)
		return inputs
