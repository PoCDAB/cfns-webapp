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
