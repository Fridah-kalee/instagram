from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile,Post
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import NewPostForm,SignUpForm,ProfileUpdateForm
from django.urls import reverse
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

def profile(request):
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user)

        if  profile_form.is_valid():
           
            profile_form.save()

            return redirect('home')

    else:
        profile_form = ProfileUpdateForm(instance=request.user)
        context = {
            
            'profile_form': profile_form
        }

    return render(request, 'profile.html', context)

def profile_update(request):
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')

    else:
        profile_form = ProfileUpdateForm(instance=request.user)

        context = {
            'profile_form': profile_form

        }

    return render(request, 'profile_update.html', context)

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
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'django_registration/registration_form.html', {'form': form})    

# def likes(request,pk):
#     # post = Post.objects.get(pk=pk)
#     post=get_object_or_404(Post, id=pk)
#     post.likes+=1
#     post.save()
#     return redirect('home')