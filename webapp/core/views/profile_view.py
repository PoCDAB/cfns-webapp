from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from base64 import b64encode
from ..forms import viewBase64AuthcodeForm

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