from typing import TypedDict, NotRequired, Optional


class DPOTableOptions(TypedDict):
    title: str
    caption: NotRequired[str]
    show_header: NotRequired[bool]
    show_footer: NotRequired[bool]
    show_lines: NotRequired[bool]
    highlight: NotRequired[bool]
    safe_box: NotRequired[bool]
