from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile,Post
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import NewPostForm,SignUpForm

# Create your views here.
@login_required(login_url='/accounts/login/')
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

def post(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
           
            image.save()
            
        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'post.html', {"form": form})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'django_registration/registration_form.html', {'form': form})    
