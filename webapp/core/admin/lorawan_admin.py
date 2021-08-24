from django.contrib import admin
from ..models import dabModel

class lorawanAdmin(admin.ModelAdmin):
    list_display = ('id', 'ack', 'msg', 'rssi', 'hdop', 'alt')
    list_filter = ()

    fieldsets = [
        ("BaseModel", {'fields': ['id', 'created_at', 'updated_at']}),
        ("LoRaWAN Model", {'fields': ['received_at', 'ack', 'msg', 'rssi', 'hdop', 'alt', 'geom']}),
    ]

    search_fields = ('id', 'ack', 'msg', 'rssi', 'hdop', 'alt')
    ordering = ('id', 'ack', 'msg', 'rssi', 'hdop', 'alt', 'created_at', 'updated_at',)
    readonly_fields = ('id', 'created_at', 'updated_at',)
    filter_horizontal = ()

    class Meta:
        model = dabModel