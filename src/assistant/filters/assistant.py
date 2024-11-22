# -*- coding: utf-8 -*-#
import django_filters

from assistant.models import AssistantProxy
from core.filters.filter_created_mixin import FilterCreatedMixin


class AssistantFilter(FilterCreatedMixin):
    """Filter class for filtering AssistantProxy instances.

    This class defines a filter for AssistantProxy instances based on certain fields.

    Attributes:
        Inherits from FilterCreatedMixin to include filter behavior based on creation date.

    Meta:
        model = AssistantProxy: Specifies the model that this filter is based on.
        fields = {...}: Defines the fields and lookup types that can be used for filtering AssistantProxy instances.
    """

    class Meta:
        model = AssistantProxy
        fields = {
            "assistant_type": ["exact"],
            "user__status": ["exact"],
            "user__email": ["exact"],
            "user__is_active": ["exact"],
        }
