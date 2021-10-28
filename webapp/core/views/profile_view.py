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
from base64 import b64encode
from ..forms import viewBase64AuthcodeForm

# returns the profile template with the Base64Authentication code form
@login_required(login_url='/login') #if not logged in redirect to /login
def profileView(request):
    form = viewBase64AuthcodeForm(request.POST)
    info_msg = None
    info_type = None

    if form.is_valid():
        if request.user.check_password(request.POST['password']):
            encodedUserAndPass = "{}:{}".format(request.user.username, request.POST['password']).encode("ascii")
            userAndPass = b64encode(encodedUserAndPass).decode("ascii")
            return render(request, 'profile.html', {'form': form, 'b64code': userAndPass})
        else:
            info_msg = 'The entered password does not match your current password...'
            info_type = 'alert-danger'

    return render(request, 'profile.html', {'form': viewBase64AuthcodeForm(), 'info_msg': info_msg, 'info_type': info_type})
