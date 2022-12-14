from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from rest_framework import mixins, serializers, viewsets

from urls.models import Url
from urls.serializers import UrlSerializer
from urls.service import UrlService


class URLViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    lookup_field = "key"
    service = UrlService()

    def perform_create(self, serializer: serializers.BaseSerializer) -> None:
        serializer.instance = self.service.create_url(**serializer.validated_data)


@cache_page(60 * 60)
def redirect_view(request, key):
    object = get_object_or_404(Url, key=key)
    object.hit = F("hit") + 1
    object.save()
    return HttpResponseRedirect(f"{object.long_url}")
