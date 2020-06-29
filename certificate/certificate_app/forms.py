from django.contrib.auth.forms import UserCreationForm as ucf
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError

class UserCreationForm(ucf):
    class Meta():
        model = User
        fields = ['email','username','first_name','last_name',
            'password1','password2']

class SignupForm(ModelForm):
    class Meta():
        model = User
        fields = ['email','username']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            msg = 'Email already exists.'
            self.add_error('email', msg)