
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


class HomeView(TemplateView):
    template_name = 'whatscooking/home.html'


##########################################################################
#                           recipe views                             #
##########################################################################

class RecipeListView(TemplateView):
    template_name = "whatscooking/recipes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = Recipe.objects.order_by('id')
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'whatscooking/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(**kwargs)
        return context


class RecipeCreate(CreateView):
    model = Recipe
    template_name = 'whatscooking/recipe_create.html'
    form_class = RecipeForm
    success_url = None
    logging.debug('RecipeCreate started!')


    def get_context_data(self, **kwargs):
        logging.debug('aaa – get_context_data')


        data = super(RecipeCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['steps'] = RecipeStepFormSet(self.request.POST)
        else:
            data['steps'] = RecipeStepFormSet()

        logging.debug('bbb – get_context_data')
        logging.debug(data)
        return data




    def form_valid(self, form):
        logging.debug('RecipeCreate form_valid')

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


class RecipeUpdate(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'whatscooking/recipe_create.html'

    def get_context_data(self, **kwargs):
        data = super(RecipeUpdate, self).get_context_data(**kwargs)
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

    def get_success_url(self):
        return reverse_lazy('whatscooking:recipe-detail', kwargs={'pk': self.object.pk})


class RecipeDelete(DeleteView):
    model = Recipe
    template_name = 'whatscooking/confirm_delete.html'
    success_url = reverse_lazy('whatscooking:recipe-home')


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = '/whatscooking/recipes/'

    def test_func(self):
        Recipe = self.get_object()
        if self.request.user == Recipe.author:
            return True
        return False



# ----------------------------------
# Ingredients
# ----------------------------------


class IngredientListView(ListView):
    model = Ingredient
    template_name = 'whatscooking/ingredients.html'
    context_object_name = 'ingredients'


class IngredientDetailView(DetailView):
    model = Ingredient


class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = ['name', 'image']
    success_url = '/whatscooking/ingredients/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IngredientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ingredient
    fields = ['name', 'image']
    success_url = '/whatscooking/ingredients/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Recipe = self.get_object()
        if self.request.user == Ingredient.author:
            return True
        return False


class IngredientDeleteView(DeleteView):
    model = Ingredient
    success_url = '/whatscooking/ingredients/'

    def test_func(self):
        Recipe = self.get_object()
        if self.request.user == Ingredient.author:
            return True
        return False


# ----------------------------------


class MeasurementListView(ListView):
    template_name = 'whatscooking/measurements.html'
    model = MeasurementUnit

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = MeasurementQuantity.objects.all()
        return context
