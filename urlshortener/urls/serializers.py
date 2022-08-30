from rest_framework import serializers

from urls.models import Url
from urls.service import UrlService


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ("key", "long_url", "hit", "created_at")
        read_only_fields = ("hit", "created_at", "key")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["short_url"] = f"http://127.0.0.1:8000/{instance.key}"
        return representation
