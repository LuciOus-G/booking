from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    carousel = models.carousel.objects.all().order_by('?')
    trip = models.Post.objects.all().order_by('-date')


    content_list = {
        'carousel': carousel,
        'trip': trip,
    }
    return render(request, 'home.html', content_list)

def detail_view(request, *ids):
    for identity in models.Post.objects.all().order_by('id'):
        ids = identity.id
        print(ids)
    post = get_object_or_404(models.Post, id=ids)
    photos = models.PostImage.objects.filter(post=post)
    return render(request, 'test.html', {
        'post':post,
        'photos':photos
    })