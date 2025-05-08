from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def blog_details(request):
    return render(request, 'blog/blog-details.html')

def search_results(request):
    return render(request, 'blog/search-results.html')

def category(request):
    return render(request, 'blog/category.html')

def author_profile(request):
    return render(request, 'blog/author-profile.html')

def not_found(request):
    return render(request, 'blog/404.html')