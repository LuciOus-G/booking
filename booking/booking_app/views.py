from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.contrib.auth.models import User
from .forms import createUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    carousel = models.carousel.objects.all().order_by('?')
    trip = models.Post.objects.all().order_by('-date')


    content_list = {
        'carousel': carousel,
        'trip': trip,
    }
    return render(request, 'home.html', content_list)

def register(request):
    if request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER'))

    forms = createUser()

    if request.method == 'POST':
        forms = createUser(request.POST)
        if forms.is_valid():
            forms.save()
            user1 = forms.cleaned_data.get('username')
            messages.success(request, user1)
            return redirect('login')

    content_list = {
        'form': forms,
    }
    return render(request, 'register.html', content_list)

def login_user(request):
    if request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER'))
    fail = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            fail = True

    content_list = {
        'fail': fail
    }

    return render(request, 'login.html', content_list)

def logout_user(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))
    print(request.META.get('HTTP_REFERER'))