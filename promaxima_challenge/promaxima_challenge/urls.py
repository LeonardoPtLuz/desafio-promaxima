
from django.contrib import admin
from django.urls import path, include
from app_promaxima import views


urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include('app_promaxima.urls')),
]
