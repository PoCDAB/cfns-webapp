from django.contrib.gis import forms
from leaflet.forms.widgets import LeafletWidget
from django.conf import settings
from ..models import geoMessageModel, geoPointModel, geoCircleModel, geoPolygonModel

message_types = [
    (0, 'Message'), # message
    (1, 'Locatie'), # x,y
    (2, 'Locatie + diameter'), # x,y,diameter
    (3, 'Polygoon'), # x1,x2,y1,y2
]

class SelectDABType(forms.Form):
    messagetype = forms.IntegerField(label='Message Type', widget=forms.Select(choices=message_types))

LEAFLET_WIDGET_ATTRS = {
    'map_height': '600px',
    'map_width': '100%',
    'map_srid': 4326,
}


class SendDABForm_message(forms.Form):
    ship_id = forms.CharField(label='Schip identifier', max_length=32)
    message = forms.CharField(label='Message', max_length=64)

    class Meta:
        model = geoMessageModel

class SendDABForm_point(forms.Form):
    ship_id = forms.CharField(label='Schip identifier', max_length=256)
    message = forms.CharField(label='Message', max_length=64)
    point = forms.PointField(label='Locatie', widget=LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS))

    class Meta:
        model = geoPointModel

class SendDABForm_circle(forms.Form):
    ship_id = forms.CharField(label='Schip identifier', max_length=256)
    radius = forms.IntegerField(label='Diameter (in meters)')
    message = forms.CharField(label='Message', max_length=64)
    point = forms.PointField(label='Locatie', widget=LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS))

    class Meta:
        model = geoCircleModel

class SendDABForm_polygon(forms.Form):
    ship_id = forms.CharField(label='Schip identifier', max_length=256)
    message = forms.CharField(label='Message', max_length=64)
    polygon = forms.PolygonField(label='Polygoon', widget=LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS))

    class Meta:
        model = geoPolygonModel
