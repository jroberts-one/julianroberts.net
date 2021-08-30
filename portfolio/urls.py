from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('marathon/', views.marathon, name='portfolio-marathon'),
]
