from django.urls import path

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
