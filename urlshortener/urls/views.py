from django.db.models import Count, F
from django.shortcuts import get_object_or_404, redirect
from rest_framework import mixins, viewsets
from rest_framework.decorators import action

from urls.models import Url
from urls.serializers import UrlSerializer


class URLViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    lookup_field = "key"


def redirect_view(request, key):
    object = get_object_or_404(Url, key=key)
    object.hit = F("hit") + 1
    object.save()
    return redirect(f"/{object.key}")
