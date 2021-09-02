from django.db import models
from django.contrib.gis.db import models as gismodels
from django.db.models import Manager as GeoManager
from .ais_encoded_model import aisEncodedModel
import json

# Database model for decoded AIS
class aisDecodedModel(aisEncodedModel):
    mmsi = models.IntegerField(null=True)
    name = models.CharField('Shipname',
        max_length=128,
        blank=True,
        null=True
    )
    geom = gismodels.PointField('Location (x,y)', null=True, blank=True,)
    course = models.FloatField('Course', null=True, blank=True,)
    objects = GeoManager()

    ack = models.IntegerField('Acknowledgement',
        blank=True,
        null=True
    )
    msg = models.IntegerField('Message',
        blank=True,
        null=True
    )
    rssi = models.IntegerField('RSSI',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Decoded AIS message'
        verbose_name_plural = 'Decoded AIS messages'
    