from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.contrib.auth.models import User
from .forms import createUser
from django.contrib import messages

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

def login(request):
    return render(request, 'login.html')