from django.contrib.gis import admin

# import DB models
from ..models import geoNotification
from ..models import AIS
from ..models import AISDecoded
from ..models import DAB

# import ADMIN-DB configs
from .dab_admin import geoNotification
from .ais_admin import AISAdmin
from .ais_admin import AISDecodedAdmin
from .dab_admin import DABAdmin

# Register DB model with correct ADMIN-DB config
admin.site.register(geoNotification, geoNotification)
admin.site.register(AIS, AISAdmin)
admin.site.register(AISDecoded, AISDecodedAdmin)
admin.site.register(DAB, DABAdmin)

