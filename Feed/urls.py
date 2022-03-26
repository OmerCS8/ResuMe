from django.urls import path
from . import views

urlpatterns = [
    path('', views.Feed, name='Feed-home'),
    path('about/', views.about, name='Feed-about'),
]