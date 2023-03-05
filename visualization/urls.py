from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
urlpatterns = [
     
     path('visualization/index',views.index, name='index')
]
