from django.urls import path
from keys.views import KeyApiView

urlpatterns = [
    path(
        "keys",
        KeyApiView.as_view(),
        name="keys",
    )
]
