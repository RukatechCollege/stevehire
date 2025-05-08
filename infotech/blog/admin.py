from django.contrib import admin
from .models import Posts, Tag, Category

# Register your models here.

admin.site.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['author', 'title','content', 'image', 'tags', 'category' 'date_posted']
search_fields =['title', 'category']

admin.site.register(Tag)
list_display = ['name']
search_fields = ['name']

admin.site.register(Category)
list_display = ['name']
search_fields = ['name']