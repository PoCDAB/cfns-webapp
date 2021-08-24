from django.db import models
from django.contrib.gis.db import models as gismodels
from django.db.models import Manager as GeoManager
from .base_model import BaseModel


class DecodedPayloadModel(gismodels.Model):
    alt = models.IntegerField(max_length=256)
    hdop = models.DecimalField(max_digits=19, decimal_places=2)
    lat = models.DecimalField(max_digits=19, decimal_places=2)
    lon = models.DecimalField(max_digits=19, decimal_places=2)

class UplinkMessageModel(gismodels.Model):
    session_key_id = models.CharField(max_length=256)
    f_port = models.IntegerField(blank=True, null=True)
    f_cnt = models.IntegerField(blank=True, null=True)
    frm_payload = models.CharField(max_length=256)

    decoded_payload = models.ForeignKey(DecodedPayloadModel, on_delete=models.CASCADE, blank=True, null=True)

class DataModel(gismodels.Model):
    type = models.CharField(related_name='@type', max_length=256)
    received_at = models.DateTimeField(blank=True, null=True)

    uplink_message = models.ForeignKey(UplinkMessageModel, on_delete=models.CASCADE, blank=True, null=True)

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
    hdop = models.DecimalField(blank=True, null=True, max_digits=19, decimal_places=2)
    alt = models.DecimalField(blank=True, null=True, max_digits=19, decimal_places=2)

    received_at = models.DateTimeField(blank=True, null=True)

    data = models.ForeignKey(DataModel, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'LoRaWAN message'
        verbose_name_plural = 'LoRaWAN messages'
