from django.contrib.gis.db import models
from fontawesome_5.fields import IconField

class FontAwesomeIcon(models.Model):
    id = models.AutoField(primary_key=True)
    icon = IconField()