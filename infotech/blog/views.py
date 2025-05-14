from django.shortcuts import render, get_object_or_404
from .models import Posts, Category, Tag
# from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def blog_details(request, pk):
    posts = get_object_or_404(Posts, pk=pk)
    category = Category.objects.all()
    tag = Tag.objects.all()
    recent_posts = Posts.objects.order_by('-id')[:5]
    return render(request, 'blog/blog-details.html',
                  {'posts':posts,
                   'category': category,
                   'tag':tag,
                   'recent_posts': recent_posts})

def search_results(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    posts = Posts.objects.all().order_by('id')

    if query:
        posts = posts.filter(title__icontains=query)

    if category_id:
        posts = posts.filter(category_id=category_id)
    
    paginator = Paginator(posts, 6)
    pageNumber = request.GET.get('page')
    pagObj = paginator.get_page(pageNumber)

    category = Category.objects.all()

    return render(request, 'blog/search-results.html',{
        'query': query,
        'pagObj': pagObj,
        'category_id': category_id,
        'category': category
    })

def category(request):
    posts = Posts.objects.all().order_by('id')
    category = Category.objects.all()
    tag = Tag.objects.all()
    recent_posts = Posts.objects.order_by('-id')[:5]
    paginator = Paginator(posts, 6)
    pageNumber = request.GET.get('page')
    pageObj = paginator.get_page(pageNumber)

    return render(request, 'blog/category.html',
                  {'posts' : posts, 
                  'category' : category,
                  'pageObj' : pageObj,
                  'tag': tag,
                  'recent_posts': recent_posts
                  })

def author_profile(request):
    return render(request, 'blog/author-profile.html')

def not_found(request):
    return render(request, 'blog/404.html')