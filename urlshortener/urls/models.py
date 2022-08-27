from django.db import models
from django.utils.translation import gettext as _

from base.models import BaseModel


class Url(BaseModel):
    long_url = models.CharField(max_length=512)
    key = models.CharField(max_length=7, unique=True)
    user_id = (
        models.PositiveIntegerField()
    )  # Probably will come from user service or auth service

    class Meta:
        verbose_name = _("url")
        verbose_name_plural = _("urls")
        indexes = [
            models.Index(
                fields=[
                    "long_url",
                ]
            ),
            models.Index(
                fields=[
                    "key",
                ]
            ),
            models.Index(
                fields=[
                    "user_id",
                ]
            ),
        ]

    def __str__(self) -> str:
        return self.key
