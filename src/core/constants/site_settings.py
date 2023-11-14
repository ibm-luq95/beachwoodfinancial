# -*- coding: utf-8 -*-#
from django.utils.text import slugify

WEB_APP_SITE_SETTINGS_KEY = "web_app_site_settings"  # this for cache
APP_CONFIGS_SETTINGS_KEY = "web_app_configs"  # this for cache
SITE_SETTINGS_DB_SLUG = slugify("web app site settings")  # this for db
APP_CONFIGS_DB_SLUG = slugify("web app configs")  # this for db

SEC_DESC_CLIENT = "client"
SEC_DESC_JOB = "job"
SEC_DESC_TASK = "task"
SEC_DESC_SPECIAL_ASSIGNMENT = "special_assignment"
SEC_DESC_REQUESTED_ASSIGNMENT = "requested_assignment"
SEC_DESC_CLIENT_ACCOUNT = "client_account"
SEC_DESC_JOB_CATEGORY = "job_category"
SEC_DESC_BOOKKEEPER = "bookkeeper"
SEC_DESC_DOCUMENT = "document"
SEC_DESC_NOTE = "note"
SEC_DESC_CLIENT_CATEGORY = "client_category"
SEC_DESC_ASSISTANT = "assistant"
SEC_DESC_MANAGER = "manager"
SEC_DESC_DISCUSSION = "discussion"
SEC_DESC_REPORT = "report"
SEC_DESC_SITE_SETTINGS = "site_settings"
SEC_DESC_APPLICATION_CONFIGURATIONS = "application_configurations"
SEC_DESC_IMPORTANT_CONTACT = "important_contact"

