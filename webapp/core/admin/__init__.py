from django.contrib.gis import admin

# import DB models
from ..models import geoMessageModel, geoPointModel, geoCircleModel, geoPolygonModel
from ..models import aisEncodedModel
from ..models import aisDecodedModel
from ..models import dabModel

# import ADMIN-DB configs
from .geo_messages_admin import baseGeoMessageAdmin, geoMessagePointNotificationAdmin, geoMessageCircleNotificationAdmin, geoMessagePolygonNotificationAdmin
from .ais_admin import aisEncodedAdmin
from .ais_admin import aisDecodedAdmin
from .dab_admin import dabAdmin

# Register DB model with correct ADMIN-DB config
admin.site.register(aisEncodedModel, aisEncodedAdmin)
admin.site.register(aisDecodedModel, aisDecodedAdmin)
admin.site.register(dabModel, dabAdmin)
admin.site.register(geoMessageModel, baseGeoMessageAdmin)
admin.site.register(geoPointModel, geoMessagePointNotificationAdmin)
admin.site.register(geoCircleModel, geoMessageCircleNotificationAdmin)
admin.site.register(geoPolygonModel, geoMessagePolygonNotificationAdmin)

