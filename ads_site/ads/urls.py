# ads/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('advertisement/<int:pk>/', views.advertisement_detail, name='advertisement_detail'),
]