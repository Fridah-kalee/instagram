from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile,Post

# Create your views here.
def home(request):
    posts = Post.all_posts()
    posts = []
    for post in posts:
    
     return render(request,'home.html')
