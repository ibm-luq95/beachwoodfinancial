# -*- coding: utf-8 -*-#
"""
File: file_types_validation.py
Author: Ibrahim Luqman
Date: 5/10/24

Description: File mime types using for validation
"""

IMAGES_FT = ("image/png", "image/jpeg", "image/jpg")

DOCUMENTS_FT = (
    "text/csv",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/vnd.oasis.opendocument.spreadsheet",
    "application/pdf",
    "text/plain",
    "application/vnd.ms-excel",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/vnd.oasis.opendocument.text",
)

IMAGES_AND_DOCS_FT = IMAGES_FT + DOCUMENTS_FT
