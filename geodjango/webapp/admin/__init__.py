from django.contrib.gis import admin

# import DB models
from ..models import AIS
from ..models import AISDecoded
from ..models import DAB
from ..models import geoNotification

# import ADMIN-DB configs
from .geo_notification_admin import geoNotificationAdmin
from .ais_admin import AISAdmin
from .ais_admin import AISDecodedAdmin
from .dab_admin import DABAdmin

# Register DB model with correct ADMIN-DB config
admin.site.register(AIS, AISAdmin)
admin.site.register(AISDecoded, AISDecodedAdmin)
admin.site.register(DAB, DABAdmin)
admin.site.register(geoNotification, geoNotificationAdmin)

