#
# CFNS - Rijkswaterstaat CIV, Delft © 2020 - 2021 <cfns@rws.nl>
#
# Copyright 2020 - 2021 Daniël Geerts <daniel.geerts@rws.nl>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

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
