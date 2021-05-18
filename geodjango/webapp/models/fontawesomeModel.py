from django.contrib.gis.db import models
from fontawesome_5.fields import IconField

class Category(models.Model):
    icon = IconField()