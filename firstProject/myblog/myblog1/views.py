# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostForm, SignUpForm, ProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def home (request):
    posts = Post.objects.all()
    return render(request, 'blog/allPost.html', {'posts': posts})

def about (request): 
    return HttpResponse("About Us page")


def detailsView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # post = Post.objects.get(pk=pk)
    return render(request, "blog/detailsView.html", {'post': post}, status=200)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    else: 
        form = PostForm()
        return render(request, 'blog/create_post.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
            form = SignUpForm()
    return render(request, "blog/signup.html", { 'form': form })

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('Profile') # 'home'
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'blog/edit_profile.html', {'form': form})
    
 
