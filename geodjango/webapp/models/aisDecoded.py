from django.db import models
from django.contrib.gis.db import models as gismodels
from django.db.models import Manager as GeoManager
from .baseModel import BaseModel
from .ais import AIS

class aisDecoded(BaseModel):
    encodedAIS = models.OneToOneField(
        AIS,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    MMSI = models.IntegerField()
    name = models.CharField(
        max_length=128,
    )

    geom = gismodels.PointField()
    course = models.FloatField()

    objects = GeoManager()

    received_from = models.CharField(
        max_length=128,
    )
    received_at = models.DateTimeField()

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Decoded AIS message'
        verbose_name_plural = 'Decoded AIS messages'