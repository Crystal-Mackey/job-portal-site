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
from django.http import request
from django.urls import path
from user import views
from job import views as job_views
from django.conf.urls import (handler404, handler500, url)

handler404 = views.handler404
handler500 = views.handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="home"),
    path("search/", job_views.search_view),
    path('create/', job_views.create_listing_view.as_view(), name="create_listing"),
    path('listing/<int:listing_id>/',
         job_views.listing_detail_view.as_view(), name="listing_detail"),
    path('reject/<int:listing_id>/<int:user_id>',
         job_views.reject_applicant_view, name="reject"),
    path('applicant/<int:listing_id>/<int:user_id>',
         job_views.accept_view, name="accept"),
    path('accepted-applicant/<int:listing_id>/<int:user_id>',
         job_views.accepted_app_view, name="accepted_app"),
    path('interviewing-applicant/<int:listing_id>/<int:user_id>',
         job_views.interviewing_view, name="interviewing"),
    path('offer-applicant/<int:listing_id>/<int:user_id>',
         job_views.offer_extended_view, name="offer-extended"),
    path("signup/", views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view.as_view(), name="logout"),
    path('profile/<str:username>/', views.profile_view, name="profile"),
    path('profile/<int:id>/edit/', views.edit_profile, name="edit_profile"),
    path('favorite/<int:listing_id>/',
         job_views.toggle_favorite, name="favorite"),
]
