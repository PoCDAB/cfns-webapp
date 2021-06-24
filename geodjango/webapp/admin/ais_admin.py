from django.contrib import admin
from ..models.ais import AIS
from ..models.aisDecoded import aisDecoded

class AISAdmin(admin.ModelAdmin):

    list_display = ('id', 'received_from', 'message',)
    list_filter = ()

    fieldsets = [
        ("BaseModel", {'fields': ['id', 'created_at', 'updated_at']}),
        ("Encoded AIS Model", {'fields': ['received_from', 'message']})
    ]

    search_fields = ('id', 'received_from', 'message',)
    ordering = ('id', 'received_from', 'message', 'created_at', 'updated_at',)
    readonly_fields = ('id', 'created_at', 'updated_at',)
    filter_horizontal = ()

    class Meta:
        model = AIS
        fields = '__all__'

class aisDecodedAdmin(admin.ModelAdmin):

    list_display = ('id', 'encodedAIS', 'mmsi', 'name', 'geom', 'course')
    list_filter = ()

    fieldsets = [
        ("BaseModel", {'fields': ['id', 'created_at', 'updated_at']}),
        ('Decoded AIS Model', {'fields': ['encodedAIS', 'mmsi', 'name', 'geom', 'course']}),
    ]

    search_fields = ('id', 'encodedAIS', 'mmsi', 'name', 'geom', 'course',)
    ordering = ('id', 'encodedAIS', 'mmsi', 'name', 'geom', 'course',)
    readonly_fields = ('id', 'encodedAIS', 'created_at', 'updated_at',)
    filter_horizontal = ()

    class Meta:
        model = aisDecoded
        fields = '__all__'