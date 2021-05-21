from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        # default=now,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        # default=now,
    )

    class Meta:
        abstract = True