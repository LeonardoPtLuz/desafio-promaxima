from django.urls import path
from app_promaxima import views

urlpatterns = [
    path('scraper/', views.scraping, name='scraping'),
]
