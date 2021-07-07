from django.contrib.gis import forms
from leaflet.forms.widgets import LeafletWidget
from django.conf import settings

message_types = [
    (0, 'Bericht'),
    (1, 'Locatie'), # x,y
    (2, 'Locatie + radius'), # x,y,radius
    (3, 'Polygoon'), # x1,x2,y1,y2
]

class SelectDABType(forms.Form):
    messagetype = forms.IntegerField(label='Message Type', widget=forms.Select(choices=message_types))

class SendDABForm_message(forms.Form):
    ship_id = forms.CharField(label='Schip identifier', max_length=256)
    message = forms.CharField(label='DAB message', max_length=256)

    class Meta:
        widgets = {'PointField': settings.LEAFLET_CONFIG}

class SendDABForm_point(forms.Form):
    ship_id = forms.CharField(label='Schip identifier', max_length=256)
    message = forms.CharField(label='DAB message', max_length=256)
    point = forms.PointField(label='Locatie')

    class Meta:
        widgets = {'PointField': settings.LEAFLET_CONFIG}

class SendDABForm_circle(forms.Form):
    ship_id = forms.CharField(label='Schip identifier', max_length=256)
    message = forms.CharField(label='DAB message', max_length=256)
    point = forms.PointField(label='Locatie')
    radius = forms.IntegerField(label='Radius (meters)')

    class Meta:
        widgets = {'PointField': settings.LEAFLET_CONFIG}

class SendDABForm_polygon(forms.Form):
    ship_id = forms.CharField(label='Schip identifier', max_length=256)
    message = forms.CharField(label='DAB message', max_length=256)
    polygon = forms.PolygonField(label='Polygoon')

    class Meta:
        widgets = {'PointField': settings.LEAFLET_CONFIG}
