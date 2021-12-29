from django.urls import path
from .views import (
    COMarathonView,
    TXMarathonView,
    HomeView,
    AboutView,
    ContactFormView
)

urlpatterns = [
    path('', HomeView.as_view(), name='portfolio-home'),
    path('about/', AboutView.as_view(), name='portfolio-about'),
    path('contact/', ContactFormView.as_view(), name='portfolio-contact'),
    path('marathon-tx/', TXMarathonView.as_view(), name='portfolio-tx-marathon'),
    path('marathon-co/', COMarathonView.as_view(), name='portfolio-co-marathon'),
]
