from django.contrib import admin
from ..models import aisEncodedModel, aisDecodedModel
from leaflet.admin import LeafletGeoAdmin

class aisDecodedAdmin(LeafletGeoAdmin):

    list_display = ('id', 'received_from', 'message', 'mmsi', 'name', 'geom', 'course')
    list_filter = ()

    fieldsets = [
        ("BaseModel", {'fields': ['id', 'created_at', 'updated_at']}),
        ('Encoded AIS Model', {'fields': ['received_from', 'message']}),
        ('Decoded AIS Model', {'fields': ['mmsi', 'name', 'geom', 'course']}),
    ]

    search_fields = ('id','received_from', 'message', 'mmsi', 'name', 'geom', 'course',)
    ordering = ('id', 'received_from', 'message','mmsi', 'name', 'geom', 'course')
    readonly_fields = ('id', 'created_at', 'updated_at',)
    filter_horizontal = ()

    class Meta:
        model = aisDecodedModel
        fields = '__all__'