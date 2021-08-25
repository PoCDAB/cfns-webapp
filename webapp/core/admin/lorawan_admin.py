from django.contrib import admin
from ..models import dabModel

class lorawanAdmin(admin.ModelAdmin):
    list_display = ('id', 'ack', 'msg', 'hdop', 'alt', 'geom')
    list_filter = ()

    fieldsets = [
        ("BaseModel", {'fields': ['id', 'created_at', 'updated_at']}),
        ("LoRaWAN Model", {'fields': ['ack', 'msg', 'hdop', 'alt', 'geom']}),
        #("Gateways", {'fields': ['gateways']}),
    ]

    search_fields = ('id', 'ack', 'msg', 'hdop', 'alt', 'gateways')
    ordering = ('id', 'ack', 'msg', 'hdop', 'alt', 'created_at', 'updated_at',)
    readonly_fields = ('id', 'created_at', 'updated_at', )#'gateways')
    filter_horizontal = ()

    class Meta:
        model = dabModel