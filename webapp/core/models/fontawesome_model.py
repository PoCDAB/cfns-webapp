from django.contrib.gis.db import models
from fontawesome_5.fields import IconField

# Database model needed to view Fontawesome icons on the webapp
class FontAwesomeIcon(models.Model):
    id = models.AutoField(primary_key=True)
    icon = IconField()