from typing import List

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True

    def save(self, update_fields: List = None, **kwargs):
        if update_fields is not None:
            update_fields.append("updated_at")
            kwargs["update_fields"] = update_fields
        super(BaseModel, self).save(**kwargs)
