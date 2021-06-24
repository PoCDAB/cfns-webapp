from django.db import models
from django.contrib.gis.db import models as gismodels
from django.db.models import Manager as GeoManager
from .baseModel import BaseModel
from .ais import AIS

class aisDecoded(BaseModel):
    id = models.AutoField(primary_key=True)

    encodedAIS = models.OneToOneField(
        AIS,
        on_delete=models.CASCADE,
        null=True
    )

    mmsi = models.IntegerField(null=True)
    name = models.CharField(
        max_length=128,
        null=True
    )
    geom = gismodels.PointField(null=True)
    course = models.FloatField(null=True)
    objects = GeoManager()

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Decoded AIS message'
        verbose_name_plural = 'Decoded AIS messages'