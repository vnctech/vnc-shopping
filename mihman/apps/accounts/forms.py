from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=255)
    mobile = forms.CharField(max_length=15)

    class Meta:
        model = MyUser
        fields = ['full_name', 'mobile', 'password1', 'password2']