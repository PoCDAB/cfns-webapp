from django.contrib import admin
from ..models.dab import DAB

class DABAdmin(admin.ModelAdmin):
    list_display = ('id', 'message_id', 'message_type', 'message', 'ship_id')
    list_filter = ()

    fieldsets = [
        (None, {'fields': ['id', 'message_id', 'message_type', 'message', 'ship_id']}),
    ]

    search_fields = ('id', 'message_id', 'message_type', 'message', 'ship_id')
    ordering = ('id', 'message_id', 'message_type', 'message', 'ship_id', 'created_at', 'updated_at',)
    readonly_fields = ('id', 'created_at', 'updated_at',)
    filter_horizontal = ()

    class Meta:
        model = DAB