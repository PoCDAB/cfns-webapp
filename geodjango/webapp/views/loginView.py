from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.GET:
                return redirect(request.GET.get('next'))
            else:
                return redirect('/profile/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def loggedoutView(request):
    logout(request)
    return render(request, 'logged_out.html')