from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

# BaseModel which can be Dependency Injected into other Models
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True