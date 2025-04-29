# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def home (request):
    posts = Post.objects.all()
    return render(request, 'blog/allPost.html', {'posts': posts})

def about (request): 
    return HttpResponse("About Us page")


def detailsView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # post = Post.objects.get(pk=pk)
    return render(request, "blog/detailsView.html", {'post': post}, status=200)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('allPost')
    else: 
        form = PostForm()
        return render(request, 'blog/create_post.html', {'form': form})

 