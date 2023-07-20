from rest_framework import serializers

from site_settings.models import SiteSettings


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        exclude = (
            "metadata",
            "is_deleted",
            "deleted_at",
        )
