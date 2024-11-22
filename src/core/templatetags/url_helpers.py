# -*- coding: utf-8 -*-#
"""
File: url_helpers.py
Author: Ibrahim Luqman
Date: 5/13/24

Description: URL helpers to handle urls processes.
"""
from typing import Optional, List, Union, Dict
from django.urls.resolvers import URLPattern, URLResolver
from uuid import UUID

from django import template
from django.template import RequestContext
from django.urls import reverse_lazy, resolvers

from beach_wood_user.models import BWUser

register = template.Library()


@register.filter(name="get_last_url_part")
def get_last_url_part(full_url: str) -> str:
    """
    This function takes a full URL as a string and returns the last part of the URL.

    Args:
        full_url (str): The full URL string from which the last part needs to be extracted.

    Returns:
        str: The last part of the URL.

    """
    last_part = full_url.rsplit("/")[-1]
    return last_part


# @register.filter(name="get_url_path_by_name")


def collect_urls(
    urls: Union[URLResolver, URLPattern, None] = None,
    namespace: Optional[str] = None,
    prefix: Optional[List[str]] = None,
) -> List[dict]:
    """
    This function collects URLs based on the input URL resolver or URL pattern.

    Args:
        urls (Union[URLResolver, URLPattern, None]): The URL resolver or pattern to collect URLs from.
        namespace (Optional[str]): The namespace for the URLs.
        prefix (Optional[List[str]]): The prefix to be added to the URLs.

    Returns:
        List[dict]: A list of dictionaries containing URL information.

    """
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
) -> Union[str, None]:
    """
    Fetches the URL based on the provided parameters.

    Args:
        context (RequestContext): The request context.
        details_url (Optional[str]): The details URL pattern.
        action_urls_pattern (Optional[str]): The action URL pattern.
        url_name (Optional[str]): The URL name.
        object_pk (Optional[UUID]): The primary key of the object.

    Returns:
        Union[str, None]: The URL path or None if no URL is found.

    """
    url_path: Union[str, None] = None

    if details_url is not None:
        url_path = reverse_lazy(details_url, kwargs={"pk": object_pk})
    elif action_urls_pattern is not None:
        url_path = reverse_lazy(action_urls_pattern, kwargs={"pk": object_pk})
    elif url_name is not None:
        if object_pk is not None:
            url_path = reverse_lazy(url_name, kwargs={"pk": object_pk})
        else:
            url_path = reverse_lazy(url_name)

    return url_path


@register.simple_tag(takes_context=True)
def fetch_app_url_for_user(
    context: RequestContext,
    app_name: str,
    path_name: str,
    user_type: Optional[str] = None,
    object_pk: Optional[UUID] = None,
) -> str:
    """
    Fetches the URL for a user based on the app name, path name, user type, and object
    primary key.

    Args:
        context (RequestContext): The request context.
        app_name (str): The name of the app.
        path_name (str): The name of the path.
        user_type (Optional[str], optional): The type of user. Defaults to None.
        object_pk (Optional[UUID], optional): The primary key of the object. Defaults to None.

    Returns:
        str: The URL path.

    """
    url_path: str = ""
    if user_type is not None:
        url_pattern: str = f"{app_name}:{user_type}:{path_name}"
    else:
        url_pattern: str = f"{app_name}:{path_name}"
    if object_pk is not None:
        url_path = reverse_lazy(url_pattern, kwargs={"pk": str(object_pk)})
    else:
        url_path = reverse_lazy(url_pattern)
    return url_path


@register.simple_tag
def fetch_user_details_url(
    base_user: str, user_object: BWUser, details_name: Optional[str] = "details"
) -> str:
    """
    Fetches the URL for user details.

    Args:
        base_user (str): The base user.
        user_object (BWUser): The user object.
        details_name (Optional[str], optional): The details name. Defaults to "details".

    Returns:
        str: The URL path.

    """
    url_path: str = ""
    user_type: str = user_object.user_type
    get_user_object = getattr(user_object, user_type, None)
    if get_user_object is not None:
        url_pattern: str = f"{base_user}:{user_type}:{details_name}"
        url_path = reverse_lazy(url_pattern, kwargs={"pk": get_user_object.pk})
    return url_path


@register.simple_tag
def fetch_drf_route_api_by_name(
    app_name: str, url_kwargs: Optional[Dict[str, str]]
) -> str:
    """
    Fetches the DRF route URL by name.

    Args:
        app_name (str): The name of the app.
        url_kwargs (Optional[Dict[str, str]]): The URL kwargs.

    Returns:
        str: The URL path.

    """
    if url_kwargs is None:
        url = reverse_lazy(app_name)
    else:
        url = reverse_lazy(app_name, kwargs={"pk": url_kwargs.get("pk")})
    return url


@register.simple_tag
def get_staff_member_update_url(user: BWUser) -> str:
    # TODO: document here
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
