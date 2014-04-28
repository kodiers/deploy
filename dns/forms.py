__author__ = 'kodiers'
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('username', 'email')