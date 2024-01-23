import json

from easyaudit.models import CRUDEvent

from core.utils import get_formatted_logger

logger = get_formatted_logger()


class CRUDEventProxy(CRUDEvent):
    class Meta:
        proxy = True

    @property
    def is_custom_deleted(self) -> bool | None:
        try:
            if self.is_update() is True:
                changed_fields_json = json.loads(self.changed_fields)
                if "is_deleted" in list(changed_fields_json.keys()):
                    if changed_fields_json.get("is_deleted")[1] == "True":
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return None
        except Exception as ex:
            logger.error(str(ex))
            return None

    @property
    def is_custom_update(self) -> bool | None:
        try:
            if self.is_update() is True:
                changed_fields_json = json.loads(self.changed_fields)
                if "is_deleted" not in list(changed_fields_json.keys()):
                    return True
                else:
                    return False
        except Exception as ex:
            logger.error(str(ex))
            return None
