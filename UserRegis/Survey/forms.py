__author__ = 'sbodduluri2'
from django import forms
from django.contrib.auth.models import User
from .models import  UserProfile
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from .models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': "form-control input-lg",'placeholder': 'username'}),
    )
    email = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': "form-control input-lg",'placeholder': 'email'}),
    )

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control input-lg",'placeholder': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control input-lg",'placeholder': 'confirm password'}),label="Confirm password")

    class Meta:
        model = User
        fields = ('username', 'email', 'password','password2')


class UserProfileForm(forms.ModelForm):
    website = forms.URLField(widget=forms.TextInput(attrs={'class': "form-control input-lg",'placeholder': 'website'}))
    class Meta:
        model = UserProfile
        #fields = ('website', 'picture')
        exclude = ('user', )





