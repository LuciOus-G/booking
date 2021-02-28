from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^/?$', views.home, name='home'),
    path('user/register', views.register, name='register'),
    path('accounts/login/', views.login_user, name='login'),
    path('user/logout', views.logout_user, name='logout'),
    path('term/condition', views.termcondition, name='term'),
    # path('booking/', views.user_booking, name='book'),
    re_path(r'^booking/mountain/(?P<slug>[\w-]+)/$',views.mountain, name='mountain'),
    re_path(r'^validation/$',views.user_booking, name='booking'),
    re_path(r'preview/$', views.preview, name='preview'),
    re_path(r'^booking/mountain/$', views.book_field, name='book_field'),
    re_path(r'^booking/list/$', views.book_list, name='booking_list')
]
