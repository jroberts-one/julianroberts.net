from django.urls import path
from .views import (
    MarathonView,
    ContactFormView
)

urlpatterns = [
    path('', ContactFormView.as_view(), name='portfolio-home'),
    path('marathon/', MarathonView.as_view(), name='portfolio-marathon'),
]
