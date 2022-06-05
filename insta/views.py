from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile,Post
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    posts = Post.all_posts()
    posts = []
    for post in posts:

        pic = Profile.objects.filter(user=post.user.id).first()
        if pic:
            pic = pic.profile_pic.url
        else:
            pic =''
        obj = dict(
            image=post.image.url,
            avatar=pic,
            name=post.title,
            author=post.user.name,
            caption=post.caption
            )

        posts.append(obj)
        return render(request,'home.html',{"posts:posts"})
