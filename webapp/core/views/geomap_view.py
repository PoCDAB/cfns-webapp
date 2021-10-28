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

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..forms import GeoviewForm

# Retrieve (filterd) AIS dataset from the database for the GIS
@login_required(login_url='/login/')
def geomapView(request):
    if request.method == 'POST':
        form = GeoviewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
          
            return render(request, 'geomap.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GeoviewForm()
    return render(request, 'geomap.html', {'form': form})
