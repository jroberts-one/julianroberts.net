
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
    View
)
from .models import *
from .forms import *
import logging
from django.urls import reverse_lazy
from django.db import transaction


# ----------------------------------
# Home
# ----------------------------------
class HomeView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    template_name = 'whatscooking/home.html'

    def test_func(self):
        return self.request.user.is_superuser


# ----------------------------------
# List Views
# ----------------------------------
class RecipeList(LoginRequiredMixin, TemplateView):
    template_name = "whatscooking/recipes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = Recipe.objects.order_by('id')
        return context


class IngredientList(LoginRequiredMixin, TemplateView):
    template_name = "whatscooking/ingredients.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = Ingredient.objects.order_by('id')
        return context


# ----------------------------------
# Detail Views
# ----------------------------------
class RecipeDetail(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'whatscooking/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RecipeDetail, self).get_context_data(**kwargs)
        return context


class IngredientDetail(LoginRequiredMixin, DetailView):
    model = Ingredient
    template_name = 'whatscooking/ingredient_detail.html'

    def get_context_data(self, **kwargs):
        context = super(IngredientDetail, self).get_context_data(**kwargs)
        return context


# ----------------------------------
# Create Views
# ----------------------------------
class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    success_url = None
    template_name = 'whatscooking/recipe_create.html'

    def get_context_data(self, **kwargs):
        data = super(RecipeCreate, self).get_context_data(**kwargs)
        data['title'] = "create"
        if self.request.POST:
            data['steps'] = RecipeStepFormSet(self.request.POST)
        else:
            data['steps'] = RecipeStepFormSet()
        print(data)
        return data

    def form_valid(self, form):
        # set the author field
        form.instance.author = self.request.user
        context = self.get_context_data()
        steps = context['steps']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if steps.is_valid():
                steps.instance = self.object
                steps.save()
        return super(RecipeCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('whatscooking:recipe-detail', kwargs={'pk': self.object.pk})


class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = ['name', 'image']
    success_url = '/whatscooking/ingredients/'
    template_name = 'whatscooking/ingredient_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# ----------------------------------
# Update Views
# ----------------------------------
class RecipeUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'whatscooking/recipe_create.html'

    def get_context_data(self, **kwargs):
        data = super(RecipeUpdate, self).get_context_data(**kwargs)
        data['title'] = "update"
        if self.request.POST:
            data['steps'] = RecipeStepFormSet(
                self.request.POST, instance=self.object)
        else:
            data['steps'] = RecipeStepFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        steps = context['steps']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if steps.is_valid():
                steps.instance = self.object
                steps.save()
        return super(RecipeUpdate, self).form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('whatscooking:recipe-detail', kwargs={'pk': self.object.pk})


class IngredientUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ingredient
    fields = ['name', 'image']
    success_url = '/whatscooking/ingredients/'
    template_name = 'whatscooking/ingredient_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Ingredient = self.get_object()
        # if self.request.user == Ingredient.author:
        #     return True
        return True


# ----------------------------------
# Update Views
# ----------------------------------
class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/whatscooking/recipes/'

    def test_func(self):
        Recipe = self.get_object()
        if self.request.user == Recipe.author:
            return True
        return False


class IngredientDelete(DeleteView):
    model = Ingredient
    success_url = '/whatscooking/ingredients/'

    def test_func(self):
        Ingredient = self.get_object()
        if self.request.user == Ingredient.author:
            return True
        return False
