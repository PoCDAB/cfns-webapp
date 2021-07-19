from django.db import models
from django.contrib.gis.db import models as gismodels
from datetime import datetime
import pytz
from .base_model import BaseModel
from .dab_model import dabModel
from .ais_encoded_model import aisEncodedModel
from .ais_decoded_model import aisDecodedModel

class geoMessageModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    dab = models.OneToOneField(
        dabModel,
        on_delete=models.CASCADE,
        null=True
    )
    aisEncoded = models.OneToOneField(
        aisEncodedModel,
        on_delete=models.CASCADE,
        null=True
    )
    aisDecoded = models.OneToOneField(
        aisDecodedModel,
        on_delete=models.CASCADE,
        null=True
    )
    message = models.CharField(max_length=256)

    class Meta:
        abstract = True

class geoPointModel(geoMessageModel):
    location = gismodels.PointField('Pivot', null=True, blank=True)

    class Meta:
        verbose_name = 'Geo Point Message'
        verbose_name_plural = 'Geo Point Messages'

class geoCircleModel(geoMessageModel):
    location = gismodels.PointField('Pivot', null=True, blank=True)
    radius = models.DecimalField(null=True, blank=True, max_digits=20, decimal_places=2)
    
    class Meta:
        verbose_name = 'Geo Circle Message'
        verbose_name_plural = 'Geo Circle Messages'

class geoPolygonModel(geoMessageModel):
    polygon = gismodels.PolygonField(null=True, blank=True)

    class Meta:
        verbose_name = 'Geo Polygon Message'
        verbose_name_plural = 'Geo Polygon Messages'