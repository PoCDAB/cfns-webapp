#
# CFNS - Rijkswaterstaat CIV, Delft © 2020 - 2021 <cfns@rws.nl>
#
# Copyright 2020 - 2021 Daniël Geerts <daniel.geerts@rws.nl>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

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
