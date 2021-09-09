from django.urls import path
from .views import (
    HomeView,
    MarathonView
)

urlpatterns = [
    path('', HomeView.as_view(), name='portfolio-home'),
    path('marathon/', MarathonView.as_view(), name='portfolio-marathon'),
]
