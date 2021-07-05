from django.contrib import admin
from ..models.geo_notification_model import geoNotification

class geoNotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'DABmessage', 'aisEncoded', 'aisDecoded')
    list_filter = ()

    fieldsets = [
        ("BaseModel", {'fields': ['id', 'created_at', 'updated_at']}),
        ("Linked to:", {'fields': ['DABmessage', 'aisEncoded', 'aisDecoded']}),
        ("Radius", {'fields': ['location', 'radius']}),
        ("SAR", {'fields': ['rightuppercorner', 'rightdowncorner', 'leftdowncorner', 'leftupcorner']})
    ]

    search_fields = ('id', 'created_at', 'updated_at', 'DABmessage', 'aisEncoded', 'aisDecoded',)
    ordering = ('id', 'created_at', 'updated_at', 'DABmessage', 'aisEncoded', 'aisDecoded',)
    readonly_fields = ('id', 'created_at', 'updated_at', 'DABmessage', 'aisEncoded', 'aisDecoded',)
    filter_horizontal = ()

    class Meta:
        model = geoNotification
        fields = '__all__'