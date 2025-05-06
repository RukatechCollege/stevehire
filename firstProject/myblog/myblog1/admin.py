from django.contrib import admin
from .models import Post, Tag

# Register your models here.

admin.site.register(Post)
list_display = ['title', 'date_posted']

admin.site.register(Tag)
list_display = ['name']
