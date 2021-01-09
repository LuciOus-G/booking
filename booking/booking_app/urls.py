from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/register', views.register, name='register'),
    path('user/login', views.login_user, name='login'),
    path('user/logout', views.logout_user, name='logout'),
    path('booking', views.user_booking, name='book'),
    path('test', views.test, name='test'),
]