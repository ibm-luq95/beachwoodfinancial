# -*- coding: utf-8 -*-#
import ast
from django import template
from django.urls import reverse_lazy, NoReverseMatch
from django.template import TemplateSyntaxError

from core.utils import get_request_context

register = template.Library()

SIZE_CLASSES = {
    "sm": "sm:max-w-md",
    "md": "sm:max-w-2xl",
    "lg": "sm:max-w-4xl",
}

ICON_CLASSES = {
    "warning": "fa-triangle-exclamation text-yellow-500",
    "info": "fa-circle-info text-blue-500",
    "success": "fa-circle-check text-green-500",
    "danger": "fa-circle-xmark text-red-500",
}

ICON_NAMES = {
    "warning": "fa-solid",
    "info": "fa-solid",
    "success": "fa-solid",
    "danger": "fa-solid",
}


@register.inclusion_tag(
    "bw_ui_components/modals/ldgf_pop_modal.html", takes_context=True
)
def ldgf_pop_modal(context, *args, **kwargs) -> dict:
    context_data = get_request_context(context, kwargs)

    modal_css_id = kwargs.get("modal_css_id")
    modal_title = kwargs.get("modal_title")
    modal_description = kwargs.get("modal_description")
    modal_icon = kwargs.get("modal_icon")
    is_form_modal = kwargs.get("is_form_modal", False)
    is_submit_btn_enabled = kwargs.get("is_submit_btn_enabled", False)
    form_object = kwargs.get("form_object")
    form_id = kwargs.get("form_id")
    form_submit_text = kwargs.get("form_submit_text")
    action_url = kwargs.get("action_url")
    action_url_pk = kwargs.get("action_url_pk")
    url_kwargs = kwargs.get("url_kwargs")
    extra_hidden_inputs = kwargs.get("extra_hidden_inputs")
    extra_hidden_inputs_markup_list = []
    backdrop = kwargs.get("backdrop", "default")
    enable_dirty_check = kwargs.get("enable_dirty_check", False)
    dynamic_src = kwargs.get("dynamic_src")
    is_only_checkbox_form = kwargs.get("is_only_checkbox_form", False)
    custom_styled_checkboxes = kwargs.get("custom_styled_checkboxes", False)
    is_upload_form = kwargs.get("is_upload_form", False)
    form_method = kwargs.get("form_method", "post")
    enable_hidden_method = kwargs.get("enable_hidden_method", False)
    enable_reset_on_close = kwargs.get("enable_reset_on_close", False)

    if not modal_css_id:
        raise TemplateSyntaxError("ldgf_pop_modal: 'modal_css_id' is required.")

    if not modal_title:
        raise TemplateSyntaxError("ldgf_pop_modal: 'modal_title' is required.")

    modal_size = kwargs.get("modal_size", "md")
    modal_size_class = SIZE_CLASSES.get(modal_size, SIZE_CLASSES["md"])

    if is_form_modal:
        if not form_object:
            raise TemplateSyntaxError(
                "ldgf_pop_modal: 'form_object' is required when 'is_form_modal=True'."
            )
        if is_submit_btn_enabled:
            if not form_id:
                raise TemplateSyntaxError(
                    "ldgf_pop_modal: 'form_id' is required when both 'is_form_modal' and 'is_submit_btn_enabled' are True."
                )
            if not form_submit_text:
                raise TemplateSyntaxError(
                    "ldgf_pop_modal: 'form_submit_text' is required when 'is_submit_btn_enabled=True'."
                )

    if extra_hidden_inputs:
        try:
            parsed = ast.literal_eval(extra_hidden_inputs)
            if not isinstance(parsed, dict):
                raise ValueError("extra_hidden_inputs must be a dict")
            for name, value in parsed.items():
                tmp_markup = f"<input type='hidden' name='{name}' value='{value}' />"
                extra_hidden_inputs_markup_list.append(tmp_markup)
        except ValueError, SyntaxError:
            raise TemplateSyntaxError(
                "ldgf_pop_modal: 'extra_hidden_inputs' must be a valid Python dict string."
            )

    resolved_action_url = None
    if action_url:
        try:
            if url_kwargs:
                resolved_action_url = reverse_lazy(action_url, kwargs=url_kwargs)
            elif action_url_pk is not None:
                resolved_action_url = reverse_lazy(
                    action_url, kwargs={"pk": action_url_pk}
                )
            else:
                resolved_action_url = reverse_lazy(action_url)
        except NoReverseMatch:
            raise TemplateSyntaxError(
                f"ldgf_pop_modal: Could not resolve URL name '{action_url}'."
            )

    icon_class = None
    icon_type = None
    if modal_icon:
        icon_type = ICON_NAMES.get(modal_icon)
        icon_class = ICON_CLASSES.get(modal_icon)

    context_data.update({
        **kwargs,
        "modal_size_class": modal_size_class,
        "extra_hidden_inputs_markup_list": extra_hidden_inputs_markup_list,
        "resolved_action_url": resolved_action_url,
        "icon_class": icon_class,
        "icon_type": icon_type,
        "enable_dirty_check": enable_dirty_check,
        "enable_reset_on_close": enable_reset_on_close,
    })

    return context_data
