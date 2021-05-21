from django.contrib import admin
from ..models.ais import AIS

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