# -*- coding: utf-8 -*-#
from typing import Union

from django.contrib.sites.models import Site

from site_settings.models import SectionDescription


def get_section_description(request) -> Union[dict, None]:
    # if request.user.is_authenticated:
    domain = request.get_host()
    site_object = Site.objects.filter(domain=domain).first()
    if site_object:
        bw_section_description = SectionDescription.objects.filter(site=site_object)
        if bw_section_description.exists():
            bw_section_description_data = dict()
            for item in bw_section_description:
                bw_section_description_data.update({item.section_title: item.description})
            return bw_section_description_data
        else:
            return dict()

    else:
        return None


def return_section_description_context(request):
    return {"bw_section_description": get_section_description(request)}
