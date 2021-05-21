from django.db import models
from .baseModel import BaseModel

class AIS(BaseModel):
    id = models.AutoField(primary_key=True)

    received_from = models.CharField(
        max_length=128,
    )

    message = models.CharField(
        max_length=256,
    )

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'AIS_message'
        verbose_name_plural = 'AIS_messages'