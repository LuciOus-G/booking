from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from . import models
from django.contrib.auth.models import User
from .forms import createUser, createBooking, testForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import F
from django.contrib.auth.decorators import login_required
from django.http import QueryDict
# Create your views here.

def home(request):
    carousel = models.carousel.objects.all().order_by('?')
    trip = models.Post.objects.all().order_by('-date')
    cc = models.Post.objects.all()
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
            current_path = request.GET.get('next', None)
            return redirect(current_path)
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


def user_booking(request):
    book = createBooking(data=request.GET)
    if request.method == 'GET':
        print(book.errors.as_data())
        print(book.is_valid())
        book = createBooking(data=request.GET)
        if book.is_valid():
            book.save()
        data = request.GET.get('booking_id', None)

    return redirect('preview/?booking_id={0}'.format(data))

def preview(request):
    data = request.GET.get('booking_id', None)
    data_db = models.booking.objects.get(booking_id=data)
    contet = {
        'data': data_db
    }
    return render(request, 'preview.html', contet)

# @login_required(redirect_field_name='mountain')
def mountain(request, slug):
    mount = models.Post.objects.get(slug=slug)
    return render(request, 'mountain.html', {'mount': mount})

def book_field(request):
    token = request.GET.get('id', None)
    if token is None:
        return redirect('/')
    db = models.Post.objects.get(Token=token)
    import string,random
    booking_id = ''.join(str(random.choice(string.digits)) for x in range(13))
    booking_id = 'AMD'+booking_id+random.choice(string.ascii_uppercase)
    context = {
        'db': db,
        'booking_id': booking_id,
        'tokrn': token
    }

    return render(request, 'booking.html', context)

def book_list(request):
    print(request.user.id)
    db = models.booking.objects.filter(customer_id=request.user.id).order_by('-date')
    print(db)
    context = {
        'datauser': db
    }
    return render(request, 'booking_list.html', context)

# Extra
def termcondition(request):
    image_db = models.PostImage.objects.all()
    return render(request, 'termcondition.html', {'image': image_db})
