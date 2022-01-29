from django.urls import path
from .views import (
    HomeView,
    COMarathonView,
    TXMarathonView
)

urlpatterns = [
    path('', HomeView.as_view(), name='health-home'),
    path('marathon-tx/', TXMarathonView.as_view(), name='portfolio-tx-marathon'),
    path('marathon-co/', COMarathonView.as_view(), name='portfolio-co-marathon'),
]
