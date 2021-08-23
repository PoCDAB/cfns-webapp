from django.contrib.gis import admin

# import DB models
from ..models import geoMessageModel, geoPointModel, geoCircleModel, geoPolygonModel
from ..models import aisDecodedModel, dabModel, lorawanModel

# import ADMIN-DB configs
from .geo_messages_admin import geoMessageNotificationAdmin, geoMessagePointNotificationAdmin, geoMessageCircleNotificationAdmin, geoMessagePolygonNotificationAdmin
from .ais_admin import aisDecodedAdmin
from .dab_admin import dabAdmin
from .lorawan_admin import lorawanAdmin

# Register DB model with correct ADMIN-DB config
admin.site.register(aisDecodedModel, aisDecodedAdmin)
admin.site.register(dabModel, dabAdmin)
admin.site.register(lorawanModel, lorawanAdmin)

admin.site.register(geoMessageModel, geoMessageNotificationAdmin)
admin.site.register(geoPointModel, geoMessagePointNotificationAdmin)
admin.site.register(geoCircleModel, geoMessageCircleNotificationAdmin)
admin.site.register(geoPolygonModel, geoMessagePolygonNotificationAdmin)

