"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from user import views as user_views
from django.conf.urls import (handler404, handler500)
# from django.views.generic import TemplateView

handler404 = user_views.handler404
handler500 = user_views.handler500

urlpatterns = [
    path('login/', user_views.login_view, name='loginview'),
    path('logout/', user_views.logout_view, name='logoutview'),
    path('register/', user_views.register_view, name='registerview'),
    path('', user_views.dashboard, name='dashboard'),
    path('notifications/', user_views.notification_view, name="notifications"),
    path('create/', user_views.create_job, name='createjob'),
    path('profile/<str:username>/', user_views.profile_detail, name='userprofile'),
    path('admin/', admin.site.urls),
]
