from django.db import models
from django.contrib.gis.db import models as gismodels
from .base_model import BaseModel
from .dab_model import dabModel
from .ais_encoded_model import aisEncodedModel
from .ais_decoded_model import aisDecodedModel

class geoMessageModel(BaseModel):
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
        verbose_name = 'Geo notification'
        verbose_name_plural = 'Geo notifications'

class geoPointModel(geoMessageModel):
    location = gismodels.PointField('Pivot', null=True, blank=True,)

class geoCircleModel(geoMessageModel):
    location = gismodels.PointField('Pivot', null=True, blank=True,)
    radius = models.DecimalField(null=True, blank=True, max_digits=20, decimal_places=2)

class geoPolygonModel(geoMessageModel):
    polygon = gismodels.PolygonField(null=True, blank=True,)