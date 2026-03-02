from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('admin/', admin.site.urls)
]