
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = 'whatscooking/home.html'
    context_object_name = 'recipes'


class UserRecipeListView(ListView):
    model = Recipe
    template_name = 'whatscooking/user_recipes.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Recipe.objects.filter(author=user).order_by('-date_created')


# detail view
class RecipeDetailView(DetailView):
    model = Recipe


# create view
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name', 'description', 'cook_time', 'serving_size', 'directions']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# update view
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Recipe = self.get_object()
        if self.request.user == Recipe.author:
            return True
        return False


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = '/whatscooking'

    def test_func(self):
        Recipe = self.get_object()
        if self.request.user == Recipe.author:
            return True
        return False
