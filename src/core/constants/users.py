# -*- coding: utf-8 -*-#

# Bookkeeper user group name
BOOKKEEPER_GROUP_NAME = "Bookkeeper Group"
ASSISTANT_GROUP_NAME = "Assistant Group"
MANAGER_GROUP_NAME = "Manager Group"
READONLY_NEW_STAFF_MEMBER_GROUP_NAME = "New Staff Readonly Group"

# User types
CON_BOOKKEEPER = "bookkeeper"
CON_ASSISTANT = "assistant"
CON_MANAGER = "manager"
CON_DEVELOPER = "developer"
CON_USER = "user"

# Permission names
ASSISTANT_FULL_MANAGER_PERMISSION_WITH_MODEL_NAME = (
    "assistant.assistant_has_full_manager_permissions"
)
ASSISTANT_FULL_MANAGER_PERMISSION_SHORT_NAME = "assistant_has_full_manager_permissions"

# Default permissions for new created staff member
DEFAULT_PERMISSIONS_NEW_STAFF_MEMBER = [
    {
        "app_label": "special_assignment",
        "model_label": "SpecialAssignmentProxy".lower(),
        "permissions_codename_labels": [
            "can_view_list",
            "view_specialassignmentproxy",
            # "special_assignment.add_specialassignment",
            "special_assignment.add_specialassignmentproxy",
        ],
    },
    {
        "app_label": "task",
        "model_label": "TaskProxy".lower(),
        "permissions_codename_labels": [
            "can_view_list",
            # "view_taskproxy",
            "task.add_taskproxy",
            "task.add_task",
        ],
    },
    {
        "app_label": "job",
        "model_label": "JobProxy".lower(),
        "permissions_codename_labels": [
            "can_view_list",
            # "view_jobproxy",
            "job.add_jobproxy",
            "job.add_job",
        ],
    },
    {
        "app_label": "discussion",
        "model_label": "DiscussionProxy".lower(),
        "permissions_codename_labels": [
            "can_view_list",
            "view_discussionproxy",
            # "discussion.add_discussion",
            "discussion.add_discussionproxy",
        ],
    },
    {
        "app_label": "note",
        "model_label": "Note".lower(),
        "permissions_codename_labels": ["can_view_list", "view_note", "note.add_note"],
    },
    {
        "app_label": "document",
        "model_label": "Document".lower(),
        "permissions_codename_labels": [
            "can_view_list",
            "view_document",
            "note.add_document",
        ],
    },
    {
        "app_label": "important_contact",
        "model_label": "ImportantContact".lower(),
        "permissions_codename_labels": ["can_view_list", "view_importantcontact"],
    },
    {
        "app_label": "client_account",
        "model_label": "ClientAccount".lower(),
        "permissions_codename_labels": ["can_view_list", "view_clientaccount"],
    },
    {
        "app_label": "client",
        "model_label": "ClientProxy".lower(),
        "permissions_codename_labels": ["can_view_list", "view_clientproxy"],
    },
]
