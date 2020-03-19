"""HireMe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
from .views import PostCreateView


urlpatterns = [
    path('ho',views.home,name="home"),
    path('new_post',views.postcreate,name="postcreate"),
    path('post_employer', views.post_employer, name="post_employer"),
    path('post_candidate', views.post_candidate, name="post_candidate"),
    path('candidate_jobs',views.candidate_jobs,name="candidate_jobs"),
    path('employer_job_applied',views.employer_job_applied,name="employer_job_applied"),
]
