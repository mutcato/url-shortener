from django.db import models
from django.utils.translation import gettext as _

from base.models import BaseModel


class Hit(BaseModel):
    url = models.ForeignKey(
        to="urls.url",
        related_name="hits",
        related_query_name="hit",
        on_delete=models.CASCADE,
    )
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=512)

    class Meta:
        verbose_name = _("hit")
        verbose_name_plural = _("hits")
        ordering = ("-created_at",)
        indexes = [
            models.Index(
                fields=[
                    "ip_address",
                    "user_agent",
                ]
            ),
            models.Index(
                fields=[
                    "-created_at",
                ]
            ),
        ]

    def __str__(self) -> str:
        return self.key
