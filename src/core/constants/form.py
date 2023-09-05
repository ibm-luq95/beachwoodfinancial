# -*- coding: utf-8 -*-#

EXCLUDED_FIELDS = [
    "metadata",
    "is_deleted",
    "slug",
    "deleted_at",
    "updated_at",
    "custom_fields",
]

# Create any user form fields
CREATE_USER_FORM_FIELDS = ["first_name", "last_name", "email", "user_type"]

# HTML form file input mime types
PDF_MIME_TYPE = "application/pdf"
DOCX_MIME_TYPE = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
DOC_MIME_TYPE = "application/msword"
CSV_MIME_TYPE = "text/csv"
PNG_MIME_TYPE = "image/png"
JPEG_MIME_TYPE = "image/jpeg"
JPG_MIME_TYPE = "image/jpg"
PPTX_MIME_TYPE = (
    "application/vnd.openxmlformats-officedocument.presentationml.presentation"
)
PPT_MIME_TYPE = "application/vnd.ms-powerpoint"
AVIF_MIME_TYPE = "image/avif"
WEBP_MIME_TYPE = "image/webp"
