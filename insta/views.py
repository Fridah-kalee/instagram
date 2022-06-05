from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile,Post
# from .forms import SignUpForm

# Create your views here.
def home(request):
    posts = Post.all_posts()
    a_posts = []
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
            author=post.user.username,
            caption=post.caption
            )

        a_posts.append(obj)
    return render(request,'home.html',{"posts":a_posts})

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})    

