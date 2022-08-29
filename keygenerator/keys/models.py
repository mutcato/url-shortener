from django.db import models


class Key(models.Model):
    key = models.CharField(max_length=7)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
