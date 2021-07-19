from django.db import models
from django.contrib.gis.db import models as gismodels
from django.db.models import Manager as GeoManager
from .base_model import BaseModel
from .ais_encoded_model import aisEncodedModel
import json
\
class aisDecodedModel(BaseModel):
    aisEncoded = models.OneToOneField(
        aisEncodedModel,
        on_delete=models.CASCADE,
        null=True
    )

    mmsi = models.IntegerField(null=True)
    name = models.CharField('Schipnaam',
        max_length=128,
        blank=True,
        null=True
    )
    geom = gismodels.PointField('Locatie', null=True, blank=True,)
    course = models.FloatField('Koers', null=True, blank=True,)
    objects = GeoManager()

    class Meta:
        verbose_name = 'Decoded AIS message'
        verbose_name_plural = 'Decoded AIS messages'
    
    def natural_key(self):
        return {'aisEncoded': {'id': self.aisEncoded.id,'message': self.aisEncoded.message,'received_from': self.aisEncoded.received_from,'received_at': self.aisEncoded.received_at}, 'mmsi': self.mmsi, 'name': self.name, 'course': self.course}
