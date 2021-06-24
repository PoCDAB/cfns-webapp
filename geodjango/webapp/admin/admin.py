from django.contrib.gis import admin

# import DB models
from ..models import WorldBorder
from ..models import AIS
from ..models import aisDecoded
from ..models import DAB

# import ADMIN-DB configs
from .ais_admin import AISAdmin
from .ais_admin import aisDecodedAdmin
from .dab_admin import DABAdmin

# Register DB model with correct ADMIN-DB config
admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(AIS, AISAdmin)
admin.site.register(aisDecoded, aisDecodedAdmin)
admin.site.register(DAB, DABAdmin)
