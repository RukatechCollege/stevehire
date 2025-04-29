from django.db import models

# Create your models here.

class Post(models.Model):
    author =models.CharField(max_length=100,null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title