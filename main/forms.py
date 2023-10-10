from dataclasses import field, fields
from django import forms
from .models import Product, Category

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProductPostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('user','name', 'description', 'details', 'image', 'category')
        

class CategoryPostForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'description', 'image')
        

