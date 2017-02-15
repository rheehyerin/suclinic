from django.shortcuts import render
from django.contrib.auth.views import login as django_login

# Create your views here.

def login(request):
    render(request, "login.html")
