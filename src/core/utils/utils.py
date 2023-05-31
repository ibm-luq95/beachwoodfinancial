# -*- coding: utf-8 -*-#
from re import sub

from django.utils.translation import gettext as _


def sort_dict(dict_object: dict) -> dict:
    res = dict()
    for k, v in sorted(dict_object.items()):
        if isinstance(v, dict):
            res[k] = sort_dict(v)
        else:
            res[k] = v
    return res


def get_trans_txt(txt) -> str:
    """
    Get text as django translated text

    Parameters
    ----------
    txt : str
        text will be translated

    Returns
    -------
    str
        translated string
    """
    return _(txt)


def foreign_key_snake_case_plural(s: str) -> str:
    """
    Generate foreign key with (s) plural name

    Parameters
    ----------
    s : str
        model related name

    Returns
    -------
    str
        return the plural name
    """
    # print(s)
    snake_name = "_".join(
        sub("([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", s.replace("-", " "))).split()
    ).lower()
    snake_name = f"{snake_name}s"
    # print(snake_name)
    return snake_name


def get_request_context(context) -> dict:
    full_dict = dict()
    for con in context:
        if isinstance(con, dict):
            full_dict.update(con)

    return full_dict
