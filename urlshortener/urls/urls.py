from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from urls.views import URLViewSet

urlpatterns = [
    path(
        "urls",
        URLViewSet.as_view({"get": "list", "post": "create"}),
        name="urls",
    ),
    path(
        "urls/<str:key>",
        URLViewSet.as_view({"get": "retrieve"}),
        name="urls",
    ),
]
