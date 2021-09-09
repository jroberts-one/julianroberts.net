from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    ListView
)
from .models import Recipe


class HomeView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'whatscooking/home.html'
    context_object_name = 'recipes'
