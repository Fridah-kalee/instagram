from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post,Profile

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=60)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
class  NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','profile',]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['profile_pic']        