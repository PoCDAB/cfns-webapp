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

from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from ..models import lorawanModel, gatewayModel, lorawanGatewayConnectionModel

class gatewaymodelInline(admin.TabularInline):
    model = gatewayModel

    list_display = ('rssi', 'snr', 'gateway_id', 'gateway_eui')

    fields = ('rssi', 'snr', 'gateway_id', 'gateway_eui')
    readonly_fields = ('rssi', 'snr', 'gateway_id', 'gateway_eui')


class lorawanGatewayConnectionModelInline(admin.TabularInline):
    model = lorawanGatewayConnectionModel
    inlines = (gatewaymodelInline,)

    list_display = ('lorawan', 'gateway')

    fields = ('lorawan', 'gateway')
    readonly_fields = ('lorawan', 'gateway')

class lorawanAdmin(LeafletGeoAdmin):
    list_display = ('id', 'ack', 'msg', 'hdop', 'alt', 'geom')
    list_filter = ()

    fieldsets = [
        ("BaseModel", {'fields': ['id', 'created_at', 'updated_at']}),
        ("LoRaWAN Model", {'fields': ['ack', 'msg', 'hdop', 'alt', 'geom']}),
    ]

    search_fields = ('id', 'ack', 'msg', 'hdop', 'alt', 'gateways')
    ordering = ('id', 'ack', 'msg', 'hdop', 'alt', 'created_at', 'updated_at',)
    readonly_fields = ('id', 'created_at', 'updated_at', )
    filter_horizontal = ()

    inlines = (lorawanGatewayConnectionModelInline,)

    class Meta:
        model = lorawanModel
