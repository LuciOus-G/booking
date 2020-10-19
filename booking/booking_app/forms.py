from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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