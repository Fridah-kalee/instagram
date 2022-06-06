from django import forms
from django.contrib.auth.models import User
from .models import Post,Profile

# class SignUpForm(forms.Form):
#     your_name=forms.CharField(label='First Name',max_length=30)
#     email=forms.EmailField(label='Email')
class  NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','profile',]