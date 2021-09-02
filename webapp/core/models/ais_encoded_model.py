from django.db import models
from .base_model import BaseModel
from django.utils import timezone

# Database model for encoded AIS
class aisEncodedModel(BaseModel):
    received_from = models.CharField(
        max_length=128,
    )

    received_at = models.DateTimeField(default=timezone.now)

    message = models.CharField(
        max_length=256,
    )

    class Meta:
        abstract = True

    class Meta:
        verbose_name = 'Encoded AIS message'
        verbose_name_plural = 'Encoded AIS messages'
