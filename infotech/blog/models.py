from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Posts(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/')
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    

    def __str__ (self):
        return self.title

# class Profile(models.Model):
#     user

