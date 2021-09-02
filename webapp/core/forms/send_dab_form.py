from django.contrib.gis import forms
from leaflet.forms.widgets import LeafletWidget
from django.conf import settings
from ..models import geoMessageModel, geoPointModel, geoCircleModel, geoPolygonModel

message_types = [
    (0, 'Message'), # message
    (1, 'Location'), # x,y
    (2, 'Location + diameter'), # x,y,diameter
    (3, 'Polygon'), # x1,x2,y1,y2
]

# Form for DAB+ type selection
class SelectDABType(forms.Form):
    messagetype = forms.IntegerField(label='Message Type', widget=forms.Select(choices=message_types))

LEAFLET_WIDGET_ATTRS = {
    'map_height': '600px',
    'map_width': '100%',
    'map_srid': 4326,
}

# Form to send message via DAB+
class SendDABForm_message(forms.Form):
    ship_id = forms.CharField(label='Ship identifier', max_length=32)
    message = forms.CharField(label='Message', max_length=64)

    class Meta:
        model = geoMessageModel

# Form to send a Point via DAB+
class SendDABForm_point(forms.Form):
    ship_id = forms.CharField(label='Ship identifier', max_length=256)
    message = forms.CharField(label='Message', max_length=64)
    point = forms.PointField(label='Location', widget=LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS))

    class Meta:
        model = geoPointModel

# Form to send a Circle via DAB+
class SendDABForm_circle(forms.Form):
    ship_id = forms.CharField(label='Ship identifier', max_length=256)
    message = forms.CharField(label='Message', max_length=64)
    radius = forms.IntegerField(label='Diameter (in meters)')
    point = forms.PointField(label='Location', widget=LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS))

    class Meta:
        model = geoCircleModel

# Form to send a Polygon via DAB+
class SendDABForm_polygon(forms.Form):
    ship_id = forms.CharField(label='Ship identifier', max_length=256)
    message = forms.CharField(label='Message', max_length=64)
    polygon = forms.PolygonField(label='Polygon', widget=LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS))

    class Meta:
        model = geoPolygonModel
