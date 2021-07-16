from django.db import models
from .base_model import BaseModel

# Database Model for the DAB+ messages
class dabModel(BaseModel):
    message_id = models.IntegerField(null=True)
    message_type = models.IntegerField()
    message = models.CharField(max_length=256)
    ship_id = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'DAB message'
        verbose_name_plural = 'DAB messages'