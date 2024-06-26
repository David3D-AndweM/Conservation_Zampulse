"""
URL configuration for Zampulse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
from django.urls import path
from userauth import views

urlpatterns = [

    path('', views.home),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginn, name='loginn'),
    path('logoutt/', views.logouttt, name='logout'),
    path('upload', views.upload, name='uploading'),
    path('like-story/<str:id>', views.likes, name='like-post'),
    path('#<str:id>', views.home_story),
    path('explore/', views.explore, name='exploring'),
    path('profile/<str:id_user>', views.profile),
    path('follow', views.follow, name='follow'),
    path('delete/<str:id>', views.delete, name='delete-post'),
    path('search-results/', views.search_results, name='search-results'),
    # path('navigate/', views.nav, name='navigate'),
    path('base/', views.base, name='base'),


]
