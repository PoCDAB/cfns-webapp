from django.contrib import admin
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

    inlines = (lorawanGatewayConnectionModelInline,)

    class Meta:
        model = lorawanModel