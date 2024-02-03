# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _
from django.db import models


class StaffMemberSocialMediaMixin(models.Model):
	facebook = models.URLField(_("facebook"), null=True, blank=True)
	twitter = models.URLField(_("twitter"), null=True, blank=True)
	youtube = models.URLField(_("youtube"), null=True, blank=True)
	instagram = models.URLField(_("instagram"), null=True, blank=True)
	linkedin = models.URLField(_("linkedin"), null=True, blank=True)
	github = models.URLField(_("github"), null=True, blank=True)
	fa_facebook_icon = models.CharField(
		_("facebook icon"), max_length=30, default="fa-brands fa-facebook", editable=False
	)
	fa_twitter_icon = models.CharField(
		_("twitter icon"), max_length=30, default="fa-brands fa-twitter", editable=False
	)
	fa_instagram_icon = models.CharField(
		_("instagram icon"),
		max_length=30,
		default="fa-brands fa-instagram",
		editable=False,
	)
	fa_linkedin_icon = models.CharField(
		_("linkedin icon"), max_length=30, default="fa-brands fa-linkedin", editable=False
	)
	fa_github_icon = models.CharField(
		_("github icon"), max_length=30, default="fa-brands fa-github", editable=False
	)

	class Meta:
		abstract = True
