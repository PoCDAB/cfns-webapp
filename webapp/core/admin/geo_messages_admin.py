from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from ..models import geoPointModel, geoCircleModel, geoPolygonModel

class geoMessagePointNotificationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'dab', 'aisEncoded', 'aisDecoded')
    list_filter = ()

    fieldsets = [
        ("BaseModel", {'fields': ['id', 'created_at', 'updated_at']}),
        ("Linked to:", {'fields': ['dab', 'aisEncoded', 'aisDecoded']}),
        ("Message:", {'fields': ['message']}),
        ("Point", {'fields': ['location']}),
    ]

    search_fields = ('id', 'created_at', 'updated_at', 'dab', 'aisEncoded', 'aisDecoded',)
    ordering = ('id', 'created_at', 'updated_at', 'dab', 'aisEncoded', 'aisDecoded',)
    readonly_fields = ('id', 'created_at', 'updated_at',)# 'dab', 'aisEncoded', 'aisDecoded',)
    filter_horizontal = ()

    class Meta:
        model = geoPointModel
        fields = '__all__'


class geoMessageCircleNotificationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'dab', 'aisEncoded', 'aisDecoded')
    list_filter = ()

    fieldsets = [
        ("BaseModel", {'fields': ['id', 'created_at', 'updated_at']}),
        ("Linked to:", {'fields': ['dab', 'aisEncoded', 'aisDecoded']}),
        ("Message:", {'fields': ['message']}),
        ("Circle", {'fields': ['location', 'radius']}),
    ]

    search_fields = ('id', 'created_at', 'updated_at', 'dab', 'aisEncoded', 'aisDecoded',)
    ordering = ('id', 'created_at', 'updated_at', 'dab', 'aisEncoded', 'aisDecoded',)
    readonly_fields = ('id', 'created_at', 'updated_at', )#'dab', 'aisEncoded', 'aisDecoded',)
    filter_horizontal = ()

    class Meta:
        model = geoCircleModel
        fields = '__all__'

class geoMessagePolygonNotificationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'dab', 'aisEncoded', 'aisDecoded')
    list_filter = ()

    fieldsets = [
        ("BaseModel", {'fields': ['id', 'created_at', 'updated_at']}),
        ("Linked to:", {'fields': ['dab', 'aisEncoded', 'aisDecoded']}),
        ("Message:", {'fields': ['message']}),
        ("Polygon", {'fields': ['polygon']})
    ]

    search_fields = ('id', 'created_at', 'updated_at', 'dab', 'aisEncoded', 'aisDecoded',)
    ordering = ('id', 'created_at', 'updated_at', 'dab', 'aisEncoded', 'aisDecoded',)
    readonly_fields = ('id', 'created_at', 'updated_at',)# 'dab', 'aisEncoded', 'aisDecoded',)
    filter_horizontal = ()

    class Meta:
        model = geoPolygonModel
        fields = '__all__'