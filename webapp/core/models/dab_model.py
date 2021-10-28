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

from django.db import models
from .base_model import BaseModel

# Database Model for the DAB+ messages
class dabModel(BaseModel):
    message_id = models.IntegerField(null=True)
    message_type = models.IntegerField()
    message = models.CharField(max_length=256)
    ship_id = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'DAB message'
        verbose_name_plural = 'DAB messages'

    def natural_key(self):
        return {'id': self.id, 'message_id':self.message_id, 'message_type':self.message_type, 'ship_id':self.ship_id, 'message':self.message}
