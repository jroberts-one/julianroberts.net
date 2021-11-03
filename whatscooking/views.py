
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
#                           Collection views                             #
##########################################################################

class CollectionListView(TemplateView):
    template_name = "whatscooking/collection_base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collections'] = Collection.objects.order_by('id')
        return context


class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'whatscooking/collection_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CollectionDetailView, self).get_context_data(**kwargs)
        return context


class CollectionCreate(CreateView):
    model = Collection
    template_name = 'whatscooking/collection_create.html'
    form_class = CollectionForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(CollectionCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['titles'] = CollectionTitleFormSet(self.request.POST)
        else:
            data['titles'] = CollectionTitleFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
        return super(CollectionCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('whatscooking:collection_detail', kwargs={'pk': self.object.pk})


class CollectionUpdate(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'whatscooking/collection_create.html'

    def get_context_data(self, **kwargs):
        data = super(CollectionUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['titles'] = CollectionTitleFormSet(
                self.request.POST, instance=self.object)
        else:
            data['titles'] = CollectionTitleFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
        return super(CollectionUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('whatscooking:collection_detail', kwargs={'pk': self.object.pk})

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(CollectionUpdate, self).dispatch(*args, **kwargs)


class CollectionDelete(DeleteView):
    model = Collection
    template_name = 'whatscooking/confirm_delete.html'
    success_url = reverse_lazy('whatscooking:homepage')


##########################################################################
#                           Recipe views                             #
##########################################################################

class RecipeListView(ListView):
    model = Recipe
    template_name = 'whatscooking/recipes.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = Recipe


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name', 'url', 'description', 'cook_time',
              'serving_size', 'image']
    success_url = '/whatscooking/recipes/'

    def form_valid(self, form):
        logging.debug(form)

        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ['name', 'url', 'description', 'cook_time',
              'serving_size', 'image']
    success_url = '/whatscooking/recipes/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['step_list'] = RecipeStep.objects.all()
        return context

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
    success_url = '/whatscooking/recipes/'

    def test_func(self):
        Recipe = self.get_object()
        if self.request.user == Recipe.author:
            return True
        return False

# ----------------------------------

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


class IngredientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
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
