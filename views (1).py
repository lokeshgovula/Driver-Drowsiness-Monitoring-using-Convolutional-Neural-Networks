from django.shortcuts import render
from users.forms import DriverRegistrationForm


def index(request):
    return render(request, 'index.html', {})


def logout(request):
    return render(request, 'index.html', {})

def AutoistLogin(request):
    return render(request, 'AutoistLogin.html', {})

def AdminLogin(request):
    return render(request, 'AdminLogin.html', {})


def AutoistRegister(request):
    form = DriverRegistrationForm()
    return render(request, 'AutoistRegister.html', {'form': form})
