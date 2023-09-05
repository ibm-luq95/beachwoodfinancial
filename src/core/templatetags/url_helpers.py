# -*- coding: utf-8 -*-#
from typing import Optional
from uuid import UUID

from django import template
from django.template import RequestContext
from django.urls import reverse_lazy, resolvers

from beach_wood_user.models import BWUser

register = template.Library()


@register.filter(name="get_last_url_part")
def get_last_url_part(full_url: str) -> str:
    last_part = full_url.rsplit("/")[-1]
    return last_part


# @register.filter(name="get_url_path_by_name")


def collect_urls(urls=None, namespace=None, prefix=None) -> list | None:
    if urls is None:
        urls = resolvers.get_resolver()
    prefix = prefix or []
    if isinstance(urls, resolvers.URLResolver):
        res = []
        for x in urls.url_patterns:
            res += collect_urls(
                x,
                namespace=urls.namespace or namespace,
                prefix=prefix + [str(urls.pattern)],
            )
        return res
    elif isinstance(urls, resolvers.URLPattern):
        return [
            {
                "namespace": namespace,
                "name": urls.name,
                "pattern": prefix + [str(urls.pattern)],
                "lookup_str": urls.lookup_str,
                "default_args": dict(urls.default_args),
            }
        ]
    else:
        raise NotImplementedError(repr(urls))


@register.simple_tag(takes_context=True)
def fetch_url_by_name_pk(
    context: RequestContext,
    details_url: Optional[str] = None,
    action_urls_pattern: Optional[str] = None,
    url_name: Optional[str] = None,
    object_pk: Optional[UUID] = None,
) -> str | None:
    url_path = ""

    if details_url is not None:
        url_path = reverse_lazy(details_url, kwargs={"pk": object_pk})
    elif action_urls_pattern is not None:
        url_path = reverse_lazy(action_urls_pattern, kwargs={"pk": object_pk})
    elif url_name is not None:
        if object_pk is not None:
            url_path = reverse_lazy(url_name, kwargs={"pk": object_pk})
        else:
            url_path = reverse_lazy(url_name)
    # debugging_print(locals())
    return url_path


@register.simple_tag(takes_context=True)
def fetch_app_url_for_user(
    context: RequestContext,
    app_name: str,
    path_name: str,
    user_type: Optional[str] = None,
    object_pk: Optional[UUID] = None,
) -> str:
    url_path = ""
    if user_type is not None:
        url_pattern = f"{app_name}:{user_type}:{path_name}"
    else:
        url_pattern = f"{app_name}:{path_name}"
    # debugging_print(locals())
    if object_pk is not None:
        url_path = reverse_lazy(url_pattern, kwargs={"pk": object_pk})
    else:
        url_path = reverse_lazy(url_pattern)
    return url_path


@register.simple_tag
def fetch_user_details_url(
    base_user: str, user_object: BWUser, details_name: Optional[str] = "details"
) -> str:
    url_path = ""
    user_type = user_object.user_type
    get_user_object = getattr(user_object, user_type, None)
    if get_user_object is not None:
        url_pattern = f"{base_user}:{user_type}:{details_name}"
        url_path = reverse_lazy(url_pattern, kwargs={"pk": get_user_object.pk})
    # debugging_print(locals())
    return url_path


@register.simple_tag
def fetch_drf_route_api_by_name(app_name: str, url_kwargs: dict) -> str:
    if not url_kwargs:
        url = reverse_lazy(app_name, kwargs={"pk": url_kwargs.get("pk")})
    else:
        url = reverse_lazy(app_name)
    return url


@register.simple_tag
def get_staff_member_update_url(user: BWUser) -> str:
    url_path = ""
    management_section = ""
    pk = ""
    match user.user_type:
        case "bookkeeper":
            management_section = "management_bookkeeper"
            pk = user.bookkeeper.pk
        case "assistant":
            management_section = "management_assistant"
            pk = user.assistant.pk
        case "manager":
            management_section = "managers"
            pk = user.manager.pk
    url_path = reverse_lazy(f"dashboard:{management_section}:update", kwargs={"pk": pk})
    return url_path
