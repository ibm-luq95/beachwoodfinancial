# -*- coding: utf-8 -*-#
from django.test import TestCase, RequestFactory, SimpleTestCase, Client
from bs4 import BeautifulSoup
from django.core import management

from beach_wood_user.forms import BWLoginForm
from beach_wood_user.management.commands import create_groups
from core.management.commands import set_site, init_cache_data
from site_settings.management.commands import init_site_settings
from beach_wood_user.models import BWUser
from django.urls import reverse_lazy

from core.utils.developments.debugging_print_object import DebuggingPrint


class TestAccessDashboard(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestAccessDashboard, cls).setUpClass()
        management.call_command(create_groups.Command())
        management.call_command(set_site.Command(), init_set_site=True)
        management.call_command(
            init_site_settings.Command(),
            init_settings_configs=True,
            site_domain="testserver",
        )
        management.call_command(
            init_cache_data.Command(),
            init_cache=True,
            pick_from_env_file=True,
            site_domain="testserver",
        )

    def setUp(self):
        self.request_factory = RequestFactory()
        self.form_data = {
            "email": "admin@admin.com",
            "password": "test123456",
            "user_type": "manager",
        }
        self.client = Client()
        self.credentials = {
            "email": "admin@admin.com",
            "password": "test123456",
            "user_type": "bookkeeper",
            # "is_active": True,
            # "is_superuser": True,
            # "is_staff": True,
            # "first_name": "Administrator",
            # "last_name": "Admin",
        }

        self.user = BWUser.objects.create_user(**self.credentials)

    def test_login_form(self):
        form = BWLoginForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_successfully_login(self):
        response = self.client.post(reverse_lazy("auth:login"), self.credentials)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("dashboard:manager:home"))

    def test_invalid_login(self):
        self.credentials.update({"password": "Dsfdf"})
        response = self.client.post(reverse_lazy("auth:login"), self.credentials)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User credentials not correct!")
