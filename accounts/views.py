from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import SignupForm
from django.contrib.auth.views import login as django_login

# Create your views here.

def login(request, template_name='accounts/login.html'):
    if request.method == 'GET':
        response = django_login(request, template_name=template_name)
    elif request.method == 'POST':
        response = django_login(request, template_name=template_name)
    return response

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            User = get_user_model()
            user = User.objects.get(username=form.cleaned_data['username'])
            form.save_m2m()
            return redirect('accounts:login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {
        'form' : form,
        })
