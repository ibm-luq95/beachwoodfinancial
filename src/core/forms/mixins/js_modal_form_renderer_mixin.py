# -*- coding: utf-8 -*-#
from typing import Type

from core.config.forms import BWFormRenderer


class BWJSModalFormRendererMixin:
    """
    Mixin class for rendering forms with a JavaScript modal.
    """

    default_renderer: Type[BWFormRenderer] = BWFormRenderer
