from django.db import models
from django.contrib.gis.db import models as gismodels
from django.db.models import Manager as GeoManager
from .base_model import BaseModel

# Database model for the gateway used as receiver for the LoRaWAN message
class gatewayModel(BaseModel):
    rssi = models.IntegerField(blank=True, null=True)
    snr = models.IntegerField(blank=True, null=True)
    gateway_id = models.CharField(blank=True, null=True, max_length=256,)
    gateway_eui = models.CharField(blank=True, null=True, max_length=256,)

# Database model for the LoRaWAN message
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
    hdop = models.DecimalField(blank=True, null=True, max_digits=19, decimal_places=16)
    alt = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)

    geom = gismodels.PointField('Location', null=True, blank=True,)
    objects = GeoManager()

    class Meta:
        verbose_name = 'LoRaWAN message'
        verbose_name_plural = 'LoRaWAN messages'

# Database model to join the LoRaWAN message with the connected gateway
class lorawanGatewayConnectionModel(BaseModel):
    lorawan = models.ForeignKey(lorawanModel, on_delete=models.CASCADE, null=True, blank=True)
    gateway = models.ForeignKey(gatewayModel, on_delete=models.CASCADE, null=True, blank=True)
