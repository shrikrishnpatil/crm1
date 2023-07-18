from django.forms import ModelForm
from .models import Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Component

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'


class ComponentForm(ModelForm):
    class Meta:
        model = Component
        fields = ['name','description','tech']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']