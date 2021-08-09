from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from ..models import geoPointModel, geoCircleModel, geoPolygonModel

class geoMessagePointNotificationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'dab', 'aisDecoded')
    list_filter = ()

    fieldsets = [
        ("BaseModel", {'fields': ['id', 'created_at', 'updated_at']}),
        ("Linked to:", {'fields': ['dab', 'aisDecoded', 'lorawan']}),
        ("Point", {'fields': ['location']}),
    ]

    search_fields = ('id', 'created_at', 'updated_at', 'dab', 'aisDecoded', 'lorawan',)
    ordering = ('id', 'dab', 'aisDecoded', 'lorawan')
    readonly_fields = ('id', 'dab', 'aisDecoded', 'lorawan', 'created_at', 'updated_at',)# 'dab', 'aisDecoded',)
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
        ("Circle", {'fields': ['location', 'radius']}),
    ]

    search_fields = ('id', 'created_at', 'updated_at', 'dab', 'aisDecoded', 'lorawan')
    ordering = ('id', 'dab', 'aisDecoded', 'lorawan')
    readonly_fields = ('id', 'dab', 'aisDecoded', 'lorawan', 'created_at', 'updated_at', )#'dab', 'aisDecoded',)
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
        ("Polygon", {'fields': ['polygon']})
    ]

    search_fields = ('id', 'created_at', 'updated_at', 'dab', 'aisDecoded', 'lorawan')
    ordering = ('id', 'dab', 'aisDecoded', 'lorawan')
    readonly_fields = ('id', 'dab', 'aisDecoded', 'lorawan', 'created_at', 'updated_at',)# 'dab', 'aisDecoded',)
    filter_horizontal = ()

    class Meta:
        model = geoPolygonModel
        fields = '__all__'