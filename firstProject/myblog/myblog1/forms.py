from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ["title", "content", 'tags' ]


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
                
        fields = ['username', 'password1', 'password2']

#



    