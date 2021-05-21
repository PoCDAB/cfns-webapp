from django.contrib.gis import admin
from ..models import WorldBorder
from ..models import AIS
from ..models import User

from .ais_admin import AISAdmin
from .user_admin import UserAdmin

admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(AIS, AISAdmin)
admin.site.register(User, UserAdmin)
