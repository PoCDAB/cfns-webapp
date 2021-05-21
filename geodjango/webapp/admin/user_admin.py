from django.contrib import admin
from ..models.user import User

class UserAdmin(admin.ModelAdmin):

    list_display = ('id', 'username', 'email','firstname', 'lastname','organisation',)
    list_filter = ('username', 'email','firstname', 'lastname','organisation',)

    fieldsets = [
        ('Account gegevens', {'fields': ['id', 'username', 'email']}),
        ('Persoon gegevens', {'fields': ['firstname', 'lastname', 'organisation']}),
    ]

    search_fields = ('id', 'username', 'email','firstname', 'lastname','organisation',)
    ordering = ('id', 'username', 'email','firstname', 'lastname','organisation',)
    readonly_fields = ('id','password')
    filter_horizontal = ()

    class Meta:
        model = User
        fields = '__all__'