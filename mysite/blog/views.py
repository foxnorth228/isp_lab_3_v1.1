from unicodedata import name
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import json

def mainPage(request):
    return render(request, 'blog/base.html')
