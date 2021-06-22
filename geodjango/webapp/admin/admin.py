from django.contrib.gis import admin
from ..models import WorldBorder
from ..models import AIS
from ..models import aisDecoded

from .ais_admin import AISAdmin
from .ais_admin import aisDecodedAdmin

admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(AIS, AISAdmin)
admin.site.register(aisDecoded, aisDecodedAdmin)
