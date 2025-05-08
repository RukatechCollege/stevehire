from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path("search_results/", views.search_results, name="search_results"),
    path("category/", views.category, name="category"),
    path('author_profile/', views.author_profile, name='author_profile'),
    path('not_found/', views.not_found, name='not_found')
]
