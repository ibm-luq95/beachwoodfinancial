# -*- coding: utf-8 -*-#
"""
File: users.py
Author: Ibrahim Luqman
Date: 5/10/24

Description: Includes constants for users and permissions 
"""

# Bookkeeper user group name
BOOKKEEPER_GROUP_NAME = "Bookkeeper Group"
ASSISTANT_GROUP_NAME = "Assistant Group"
MANAGER_GROUP_NAME = "Manager Group"
READONLY_NEW_STAFF_MEMBER_GROUP_NAME = "New Staff Readonly Group"

# User types
CON_BOOKKEEPER = "bookkeeper"
CON_ASSISTANT = "assistant"
CON_MANAGER = "manager"
CON_CFO = "cfo"
CON_DEVELOPER = "developer"
CON_USER = "user"

# Permission names
ASSISTANT_FULL_MANAGER_PERMISSION_WITH_MODEL_NAME = (
    "assistant.assistant_has_full_manager_permissions"
)
ASSISTANT_FULL_MANAGER_PERMISSION_SHORT_NAME = "assistant_has_full_manager_permissions"

BOOKKEEPER_PERMISSION = "bookkeeper_user"
ASSISTANT_PERMISSION = "assistant_user"
MANAGER_PERMISSION = "manager_user"

# Default permissions for new created staff member
DEFAULT_PERMISSIONS_NEW_STAFF_MEMBER = [
    {
        "app_label": "special_assignment",
        "model_label": "SpecialAssignment".lower(),
        "permissions_codename_labels": [
            "can_view_list",
            "view_specialassignment",
            # "special_assignment.add_specialassignment",
            "add_specialassignment",
            "view_specialassignment",
            "change_specialassignment",
            "delete_specialassignment",
        ],
    },
    {
        "app_label": "task",
        "model_label": "Task".lower(),
        "permissions_codename_labels": [
            "can_view_list",
            # "view_taskproxy",
            "add_task",
            "view_task",
            "change_task",
            "delete_task",
            # "task.add_task",
        ],
    },
    {
        "app_label": "job",
        "model_label": "Job".lower(),
        "permissions_codename_labels": [
            "can_view_list",
            # "view_jobproxy",
            # "job.add_job",
            "add_job",
            "view_job",
            "change_job",
            "delete_job",
        ],
    },
    {
        "app_label": "discussion",
        "model_label": "Discussion".lower(),
        "permissions_codename_labels": [
            "can_view_list",
            "view_discussion",
            # "discussion.add_discussion",
            "add_discussion",
            "view_discussion",
            "change_discussion",
            "delete_discussion",
        ],
    },
    {
        "app_label": "note",
        "model_label": "Note".lower(),
        "permissions_codename_labels": [
            "can_view_list",
            "view_note",
            "add_note",
            "delete_note",
            "change_note",
        ],
    },
    {
        "app_label": "document",
        "model_label": "Document".lower(),
        "permissions_codename_labels": [
            "can_view_list",
            "view_document",
            "add_document",
            "delete_document",
            "change_document",
        ],
    },
    {
        "app_label": "important_contact",
        "model_label": "ImportantContact".lower(),
        "permissions_codename_labels": [
            "can_view_list",
            "view_importantcontact",
            "add_importantcontact",
            "change_importantcontact",
            "delete_importantcontact",
        ],
    },
    {
        "app_label": "client_account",
        "model_label": "ClientAccount".lower(),
        "permissions_codename_labels": [
            "can_view_list",
            "view_clientaccount",
            "add_clientaccount",
            "change_clientaccount",
            "delete_clientaccount",
        ],
    },
    {
        "app_label": "client",
        "model_label": "Client".lower(),
        "permissions_codename_labels": [
            "can_view_list",
            "view_client",
            "add_client",
            "change_client",
            "delete_client",
        ],
        "extra_permissions": {"codename_labels": []},
    },
    {
        "app_label": "staff_briefcase",
        "model_label": "staffbriefcase".lower(),
        "permissions_codename_labels": [
            # "can_view_list",
            "view_staffbriefcase",
            "add_staffbriefcase",
            "change_staffbriefcase",
            "delete_staffbriefcase",
        ],
        "extra_permissions": {"codename_labels": []},
    },
    {
        "app_label": "staff_briefcase",
        "model_label": "staffaccounts".lower(),
        "permissions_codename_labels": [
            # "can_view_list",
            "view_staffaccounts",
            "add_staffaccounts",
            "change_staffaccounts",
            "delete_staffaccounts",
        ],
        "extra_permissions": {"codename_labels": []},
    },
    {
        "app_label": "staff_briefcase",
        "model_label": "staffdocuments".lower(),
        "permissions_codename_labels": [
            # "can_view_list",
            "view_staffdocuments",
            "add_staffdocuments",
            "change_staffdocuments",
            "delete_staffdocuments",
        ],
        "extra_permissions": {"codename_labels": []},
    },
    {
        "app_label": "staff_briefcase",
        "model_label": "staffnotes".lower(),
        "permissions_codename_labels": [
            # "can_view_list",
            "view_staffnotes",
            "add_staffnotes",
            "change_staffnotes",
            "delete_staffnotes",
        ],
        "extra_permissions": {"codename_labels": []},
    },
]
DEFAULT_PERMISSIONS_NEW_STAFF_MEMBER = sorted(
    DEFAULT_PERMISSIONS_NEW_STAFF_MEMBER, key=lambda x: x.get("app_label")
)
