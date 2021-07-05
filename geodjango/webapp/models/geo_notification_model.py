from django.db import models
from django.contrib.gis.db import models as gismodels
from .base_model import BaseModel
from ..models import *

# Database Model for the notification on the GIS
class geoNotification(BaseModel):
    id = models.AutoField(primary_key=True)

    DABmessage = models.OneToOneField(
        DAB,
        on_delete=models.CASCADE,
        null=True
    )

    aisEncoded = models.OneToOneField(
        AIS,
        on_delete=models.CASCADE,
        null=True
    )

    aisDecoded = models.OneToOneField(
        AISDecoded,
        on_delete=models.CASCADE,
        null=True
    )

    location = gismodels.PointField('Pivot', null=True, blank=True)
    radius = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=2)

    rightuppercorner = models.CharField(max_length=256, null=True, blank=True)
    rightdowncorner = models.CharField(max_length=256, null=True, blank=True)
    leftdowncorner = models.CharField(max_length=256, null=True, blank=True)
    leftupcorner = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        verbose_name = 'Geo notification'
        verbose_name_plural = 'Geo notifications'
