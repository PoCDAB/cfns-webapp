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

import json
from django.contrib.gis.geos import Point, Polygon, GEOSGeometry
from ..models import aisDecodedModel, lorawanModel
from ..models import geoMessageModel, geoPointModel, geoCircleModel, geoPolygonModel
from re import search

##
# Function creates GeoData object in database. Switches between different kind of GeoTypes
##
def createGeoData(dabmessage, POSTdata):
    if dabmessage.message_type == 0:
        return geoMessageModel.objects.create(
            dab = dabmessage,
            message = POSTdata['message'],
        )
    elif dabmessage.message_type == 1:
        return geoPointModel.objects.create(
            dab = dabmessage,
            location = POSTdata['point'],
            message = POSTdata['message'],
        )
    elif dabmessage.message_type == 2:
        return geoCircleModel.objects.create(
            dab = dabmessage,
            location = POSTdata['point'],
            radius = POSTdata["radius"],
            message = POSTdata['message'],
        )
    elif dabmessage.message_type == 3:
        return geoPolygonModel.objects.create(
            dab = dabmessage,
            polygon = POSTdata['polygon'],
            message = POSTdata['message'],
        )
    else:
        return None

##
# Function can alter a GeoData object. Add new technologie
##
def alterGeoData(parent, object):
    if type(object) is aisDecodedModel:
        parent.aisDecoded = object
    if type(object) is lorawanModel:
        parent.lorawan = object
    parent.save()
    return parent
