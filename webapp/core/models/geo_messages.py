from django.db import models
from django.contrib.gis.db import models as gismodels
from datetime import datetime
import pytz
from .base_model import BaseModel
from .fontawesome_model import FontAwesomeIcon
from .dab_model import dabModel
from .ais_decoded_model import aisDecodedModel
from .lorawan_model import lorawanModel

# Database model for the baseGeoModel
class geoModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    dab = models.OneToOneField(
        dabModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    aisDecoded = models.OneToOneField(
        aisDecodedModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    lorawan = models.OneToOneField(
        lorawanModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    font_awesome_icon = FontAwesomeIcon()
    font_awesome_iconcolor = models.CharField(max_length=256)

    class Meta:
        abstract = True

# Database model for the geoMessage
class geoMessageModel(geoModel):
    message = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Geo Message'
        verbose_name_plural = 'Geo Messages'
    def natural_key(self):
        return {'id': self.id, 'dab':self.dab,  'ais':self.aisDecoded, 'lorawan': self.lorawan, 'message': self.message}

# Database model for the geoPoint
class geoPointModel(geoModel):
    location = gismodels.PointField('Pivot', null=True, blank=True)
    message = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Geo Point Message'
        verbose_name_plural = 'Geo Point Messages'
    def natural_key(self):
        return {'id': self.id, 'dab':self.dab,  'ais':self.aisDecoded, 'lorawan': self.lorawan, 'location':self.location, 'message': self.message}

# Database model for the geoCircle
class geoCircleModel(geoModel):
    location = gismodels.PointField('Pivot', null=True, blank=True)
    radius = models.DecimalField(null=True, blank=True, max_digits=20, decimal_places=2)
    message = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Geo Circle Message'
        verbose_name_plural = 'Geo Circle Messages'
    def natural_key(self):
        return {'id': self.id, 'dab':self.dab, 'ais':self.aisDecoded, 'lorawan': self.lorawan, 'location':self.location, 'radius':self.radius, 'message': self.message}

# Database model for the geoPolygon
class geoPolygonModel(geoModel):
    polygon = gismodels.PolygonField(null=True, blank=True)
    message = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Geo Polygon Message'
        verbose_name_plural = 'Geo Polygon Messages'
    def natural_key(self):
        return {'id': self.id, 'dab':self.dab, 'ais':self.aisDecoded, 'lorawan': self.lorawan, 'polygon':self.polygon, 'message': self.message}