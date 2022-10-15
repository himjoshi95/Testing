from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.core.exceptions import ValidationError



class TodoForm(forms.Form):
    task = forms.CharField(max_length=50)
    deadline= forms.DateField()

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email' ,'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']




