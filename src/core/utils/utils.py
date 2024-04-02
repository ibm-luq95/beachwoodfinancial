# -*- coding: utf-8 -*-#
from re import sub
import calendar
from typing import Optional

from django.utils.translation import gettext as _


def sort_dict(dict_object: dict) -> dict:
    """
    Sorts a dictionary object recursively based on keys and returns the sorted dictionary.

    :param dict_object: a dictionary to be sorted
    :return: a sorted dictionary
    """
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


def get_request_context(context, kwargs_element) -> dict:
    full_dict = dict()
    data_aria_attributes = ""
    for con in context:
        if isinstance(con, dict):
            full_dict.update(con)
    for key, value in kwargs_element.items():
        if key.startswith("data_") or key.startswith("aria_"):
            new_data_name = key.replace("_", "-")
            data_aria_attributes += f"{new_data_name}={value} "
    data_aria_attributes = data_aria_attributes.strip()
    full_dict.update({"data_aria_attributes": data_aria_attributes})
    return full_dict


def get_months_abbr(
    year: Optional[int | str] = None, return_months_idxs: bool = False
) -> tuple:
    """
    Get months abbreviations as tuple of months abbreviations or indexes
    Parameters
    ----------
    year: int | str = Year passed
    return_months_idxs: bool = if true will return tuple of indexes

    Returns
    -------
    tuple
    """
    data = []
    base_months = tuple(calendar.month_abbr)
    for month in base_months:
        if month != "":
            if year is not None:
                data.append(f"{month} - {year}")
            else:
                data.append(month)
    if return_months_idxs is False:
        return tuple(data)
    else:
        return tuple(range(1, 13))


def get_months_dict() -> dict[str, list]:
    """
    Return a dictionary mapping month numbers to empty lists.
    """
    months_data = get_months_abbr(return_months_idxs=True)
    months_dict = dict()
    for i, month in enumerate(months_data):
        months_dict[str(i + 1)] = []
    return months_dict
