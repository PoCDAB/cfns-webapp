from django.db import models
from django.contrib.gis.db import models as gismodels
from django.db.models import Manager as GeoManager
from .base_model import BaseModel

class gatewayModel(BaseModel):
    rssi = models.IntegerField(blank=True, null=True)
    snr = models.IntegerField(blank=True, null=True)
    gateway_id = models.CharField(blank=True, null=True, max_length=256,)
    gateway_eui = models.CharField(blank=True, null=True, max_length=256,)

class lorawanModel(BaseModel):
    ack = models.IntegerField('Acknowledgement',
        blank=True,
        null=True
    )
    msg = models.CharField('Message',
        blank=True,
        null=True,
        max_length=256,
    )
    hdop = models.DecimalField(blank=True, null=True, max_digits=19, decimal_places=2)
    alt = models.DecimalField(blank=True, null=True, max_digits=19, decimal_places=2)

    gateways = models.ManyToManyField(gatewayModel)

    geom = gismodels.PointField('Location', null=True, blank=True,)
    objects = GeoManager()

    class Meta:
        verbose_name = 'LoRaWAN message'
        verbose_name_plural = 'LoRaWAN messages'
