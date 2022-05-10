from unicodedata import name
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.utils import timezone
from .forms import SignupForm, AuthForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import json
#import logging
#import configparser


#config = configparser.ConfigParser()
#config.read('cnf.ini')
#logging.basicConfig(
#    level=config['LOGGING']['level'],
#    filename=config['LOGGING']['filename']
#)
#log = logging.getLogger(__name__)
def mainPage(request):
    return render(request, 'blog/base.html', {'path': f"http://{request.get_host()}/blog"})

def register_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
#            p = Process(target=log.info(f'{request.user} registred'))
            form.save()
            return redirect('login')
    else:
        form = SignupForm(request.POST)
    return render(
        request,
        'register/registration.html',
        {
            'form': form,
            'path': f"http://{request.get_host()}/blog",
        }
    )

def login_user(request):
    if request.user.is_authenticated:
        return redirect('post_list')
    if request.method == 'POST':
        form = AuthForm(request, request.POST)
        print("form: ", form.data)
        print('post: ', request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('post_list')
    else:
        form = AuthForm()
    return render(
        request,
        'register/login.html',
        {
            'form': form,
            'path': f"http://{request.get_host()}/blog",
        }
    )

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')

