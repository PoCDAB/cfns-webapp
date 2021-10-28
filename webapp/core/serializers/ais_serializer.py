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

from rest_framework import serializers
from django.contrib.gis.geos import Point
from pyais import decode_msg
from ..models import aisDecodedModel

# This AIS serializer is activated when an API call is received
# It decoded the AIS message and puts the correct fields into a new DB record
class aisSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        decodedAIS = aisDecodedModel.objects.create(**validated_data)
        msg = decode_msg(validated_data['message'])
        if 'mmsi' in msg:
            setattr(decodedAIS, 'mmsi', msg['mmsi'])
        if 'shipname' in msg:
            setattr(decodedAIS, 'name', msg['shipname'])
        if 'lat' and 'lon' in msg:
            setattr(decodedAIS, 'geom', Point(msg['lon'], msg['lat'])) # x = lon, y = lat
        if 'course' in msg:
            setattr(decodedAIS, 'course', msg['course'])
        decodedAIS.save()
        return decodedAIS

    class Meta:
        model = aisDecodedModel
        fields = ['id', 'received_from', 'received_at', 'message','mmsi', 'name', 'geom', 'course', 'ack', 'msg', 'rssi', 'created_at', 'updated_at']
