from rest_framework import serializers

from urls.models import Url
from urls.service import UrlService


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ("key", "long_url", "hit", "created_at")
        read_only_fields = ("hit", "created_at")

    def to_internal_value(self, data):
        url_service = UrlService()
        data._mutable = True
        data["key"] = url_service.get_key()
        return super().to_internal_value(data)
