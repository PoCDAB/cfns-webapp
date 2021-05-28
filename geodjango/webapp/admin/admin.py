from django.contrib.gis import admin
from ..models import WorldBorder
from ..models import AIS

from .ais_admin import AISAdmin

admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(AIS, AISAdmin)
