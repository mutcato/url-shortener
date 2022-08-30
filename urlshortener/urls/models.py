from base.models import BaseModel
from django.db import models
from django.utils.translation import gettext as _


class Url(BaseModel):
    long_url = models.URLField(max_length=512)
    key = models.CharField(max_length=7, unique=True)
    hit = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = _("url")
        verbose_name_plural = _("urls")
        indexes = [
            models.Index(
                fields=[
                    "long_url",
                ]
            ),
        ]

    def __str__(self) -> str:
        return self.key
