"""toqa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home import forms, views as Hviews
from loggedIn import views as loggedinViews
from django.contrib.auth import views as auth_v

from home.forms import loginForm


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    
    path('home/', Hviews.home_page, name='home'),

    path('login/', auth_v.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True,
        authentication_form=loginForm), name='login'),

    path('loading/' , Hviews.loadingPage, name="loading"),

    path('logout/', auth_v.LogoutView.as_view(), name='logout'),

    path('teacher/' , loggedinViews.teacherPage, name="teacher"),
    
    path('manage/' , loggedinViews.manage, name="manage"),

]
