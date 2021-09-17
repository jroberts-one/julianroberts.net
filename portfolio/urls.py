from django.urls import path
from .views import (
    MarathonView,
    HomeView,
    AboutView,
    ContactFormView
)

urlpatterns = [
    path('', HomeView.as_view(), name='portfolio-home'),
    path('about/', AboutView.as_view(), name='portfolio-about'),
    path('contact/', ContactFormView.as_view(), name='portfolio-contact'),
    path('marathon/', MarathonView.as_view(), name='portfolio-marathon'),
]
