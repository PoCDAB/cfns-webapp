from django.contrib import admin
from ..models import aisEncodedModel, aisDecodedModel

class aisEncodedAdmin(admin.ModelAdmin):

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
        model = aisEncodedModel
        fields = '__all__'

class aisDecodedAdmin(admin.ModelAdmin):

    list_display = ('id', 'aisEncoded', 'mmsi', 'name', 'geom', 'course')
    list_filter = ()

    fieldsets = [
        ("BaseModel", {'fields': ['id', 'created_at', 'updated_at']}),
        ('Decoded AIS Model', {'fields': ['aisEncoded', 'mmsi', 'name', 'geom', 'course']}),
    ]

    search_fields = ('id', 'aisEncoded', 'mmsi', 'name', 'geom', 'course',)
    ordering = ('id', 'aisEncoded', 'mmsi', 'name', 'geom', 'course',)
    readonly_fields = ('id', 'aisEncoded', 'created_at', 'updated_at',)
    filter_horizontal = ()

    class Meta:
        model = aisDecodedModel
        fields = '__all__'