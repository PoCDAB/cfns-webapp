from django.db import models
from django.contrib.gis.db import models as gismodels
from django.db.models import Manager as GeoManager
from .base_model import BaseModel

class lorawanModel(BaseModel):
    geom = gismodels.PointField('Location', null=True, blank=True,)
    objects = GeoManager()

    ack = models.IntegerField('Acknowledgement',
        blank=True,
        null=True
    )
    msg = models.CharField('Message',
        blank=True,
        null=True,
        max_length=256,
    )
    rssi = models.IntegerField(blank=True, null=True)
    hdop = models.IntegerField(blank=True, null=True)
    alt = models.IntegerField(blank=True, null=True)

    received_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'LoRaWAN message'
        verbose_name_plural = 'LoRaWAN messages'
