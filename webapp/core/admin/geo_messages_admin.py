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
from ..models import geoMessageModel, geoPointModel, geoCircleModel, geoPolygonModel

class geoMessageNotificationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'dab', 'aisDecoded')
    list_filter = ()

    fieldsets = [
        ("BaseModel", {'fields': ['id', 'created_at', 'updated_at']}),
        ("Linked to:", {'fields': ['dab', 'aisDecoded', 'lorawan']}),
        ("Message", {'fields': ['message']}),
    ]

    search_fields = ('id', 'created_at', 'updated_at', 'dab', 'aisDecoded', 'lorawan',)
    ordering = ('id', 'dab', 'aisDecoded', 'lorawan')
    readonly_fields = ('id', 'dab', 'aisDecoded', 'lorawan', 'created_at', 'updated_at',)
    filter_horizontal = ()

    class Meta:
        model = geoMessageModel
        fields = '__all__'

class geoMessagePointNotificationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'dab', 'aisDecoded')
    list_filter = ()

    fieldsets = [
        ("BaseModel", {'fields': ['id', 'created_at', 'updated_at']}),
        ("Linked to:", {'fields': ['dab', 'aisDecoded', 'lorawan']}),
        ("PointMessage", {'fields': ['message', 'location']}),
    ]

    search_fields = ('id', 'created_at', 'updated_at', 'dab', 'aisDecoded', 'lorawan',)
    ordering = ('id', 'dab', 'aisDecoded', 'lorawan')
    readonly_fields = ('id', 'dab', 'aisDecoded', 'lorawan', 'created_at', 'updated_at',)
    filter_horizontal = ()

    class Meta:
        model = geoPointModel
        fields = '__all__'


class geoMessageCircleNotificationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'dab', 'aisDecoded')
    list_filter = ()

    fieldsets = [
        ("BaseModel", {'fields': ['id', 'created_at', 'updated_at']}),
        ("Linked to:", {'fields': ['dab', 'aisDecoded', 'lorawan']}),
        ("CircleMessage", {'fields': ['message', 'location', 'radius']}),
    ]

    search_fields = ('id', 'created_at', 'updated_at', 'dab', 'aisDecoded', 'lorawan')
    ordering = ('id', 'dab', 'aisDecoded', 'lorawan')
    readonly_fields = ('id', 'dab', 'aisDecoded', 'lorawan', 'created_at', 'updated_at', )
    filter_horizontal = ()

    class Meta:
        model = geoCircleModel
        fields = '__all__'

class geoMessagePolygonNotificationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'dab', 'aisDecoded')
    list_filter = ()

    fieldsets = [
        ("BaseModel", {'fields': ['id', 'created_at', 'updated_at']}),
        ("Linked to:", {'fields': ['dab', 'aisDecoded', 'lorawan']}),
        ("PolygonMessage", {'fields': ['message', 'polygon']})
    ]

    search_fields = ('id', 'created_at', 'updated_at', 'dab', 'aisDecoded', 'lorawan')
    ordering = ('id', 'dab', 'aisDecoded', 'lorawan')
    readonly_fields = ('id', 'dab', 'aisDecoded', 'lorawan', 'created_at', 'updated_at',)
    filter_horizontal = ()

    class Meta:
        model = geoPolygonModel
        fields = '__all__'
