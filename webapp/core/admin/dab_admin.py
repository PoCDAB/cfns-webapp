from django.contrib import admin
from ..models import dabModel

class dabAdmin(admin.ModelAdmin):
    list_display = ('id', 'message_id', 'message_type', 'message', 'ship_id')
    list_filter = ()

    fieldsets = [
        ("BaseModel", {'fields': ['id', 'created_at', 'updated_at']}),
        ("DAB Model", {'fields': ['message_id', 'message_type', 'message', 'ship_id']}),
    ]

    search_fields = ('id', 'message_id', 'message_type', 'message', 'ship_id')
    ordering = ('id', 'message_id', 'message_type', 'message', 'ship_id', 'created_at', 'updated_at',)
    readonly_fields = ('id', 'created_at', 'updated_at',)
    filter_horizontal = ()

    class Meta:
        model = dabModel