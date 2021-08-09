from django.db import models
from django.contrib.gis.db import models as gismodels
from django.db.models import Manager as GeoManager
from .base_model import BaseModel
from .ais_encoded_model import aisEncodedModel
import json

class lorawanModel(BaseModel):
    geom = gismodels.PointField('Location', null=True, blank=True,)
    objects = GeoManager()

    ack = models.IntegerField('Acknowledgement',
        blank=True,
        null=True
    )
    msg = models.IntegerField('Message',
        blank=True,
        null=True
    )
    rssi = models.IntegerField(blank=True, null=True)
    hdop = models.IntegerField(blank=True, null=True)
    alt = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'LoRaWAN message'
        verbose_name_plural = 'LoRaWAN messages'
