from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('detail/<int:pk>/', views.detailsView, name="detailsView"),
    path('post/new/', views.create_post, name="create_post"),
    path('account/signup/', views.signup, name='signup'),
    # path('logout/', views.logout, name='logout')
    #  path('accounts/login/', LoginView.as_view(), name='login'),
]

# redirect on create_post 