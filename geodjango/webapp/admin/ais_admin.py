from django.contrib import admin
from ..models.ais import AIS
from ..models.aisDecoded import aisDecoded

class AISAdmin(admin.ModelAdmin):

    list_display = ('id', 'received_from', 'message',)
    list_filter = ('received_from', 'message',)

    fieldsets = [
        (None, {'fields': ['id', 'received_from', 'message']}),
        (None, {'fields': ['created_at', 'updated_at']})
    ]

    search_fields = ('id', 'received_from', 'message',)
    ordering = ('id', 'received_from', 'message', 'created_at', 'updated_at',)
    readonly_fields = ('id', 'created_at', 'updated_at',)
    filter_horizontal = ()

    class Meta:
        model = AIS
        fields = '__all__'

class aisDecodedAdmin(admin.ModelAdmin):

    list_display = ('encodedAIS', 'mmsi', 'name', 'geom', 'course', 'received_from', 'received_at')
    list_filter = ('encodedAIS', 'mmsi', 'name', 'geom', 'course', 'received_from', 'received_at')

    fieldsets = [
        ('Encoded AIS', {'fields': ['encodedAIS','received_from', 'received_at']}),
        ('Decoded AIS', {'fields': ['mmsi', 'name', 'geom', 'course']}),
    ]

    search_fields = ('encodedAIS', 'mmsi', 'name', 'geom', 'course', 'received_from', 'received_at')
    ordering = ('encodedAIS', 'mmsi', 'name', 'geom', 'course', 'received_from', 'received_at')
    readonly_fields = ('encodedAIS', 'mmsi', 'name', 'geom', 'course', 'received_from', 'received_at')
    filter_horizontal = ()

    class Meta:
        model = aisDecoded
        fields = '__all__'