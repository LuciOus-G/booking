from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class createBooking(ModelForm):
    class Meta:
        model = models.booking
        fields = [
            'name_trip',
            'seat_available','price','place_born','day_born','gender','address',
            'phone1','people',
            'user_name'
            ,'customer_id','booking_id','trip_id','departure_day','meeting_point',
            'total_price','email'
        ]

class createUser(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]
    def email_valid(self):
        email = self.cleaned_data.get('email')
        count = User.objects.filter(email=email).count()
        if count > 0:
            raise forms.ValidationError('already')
        return email

class testForm(ModelForm):
    class Meta:
        model = models.test
        fields = ['name']
