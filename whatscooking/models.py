from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import URLValidator
from django.forms.models import inlineformset_factory


class MeasurementUnit(models.Model):
    unit = models.CharField(max_length=100)
    metric = models.BooleanField(default=True)


class MeasurementQuantity(models.Model):
    quantity = models.CharField(max_length=100)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(
        default='default_ingredient.png', upload_to='ingredient_pics')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient-detail', kwargs={'pk': self.pk})


class PantryIngredient(models.Model):
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Recipe(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cook_time = models.CharField(max_length=20, null=True)
    serving_size = models.CharField(max_length=20, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    image = models.ImageField(
        default='default_recipe.png', upload_to='recipe_pics')
    url = models.CharField(
        validators=[URLValidator()], null=True, max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})


class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    description = models.TextField()
    order = models.IntegerField()


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)
    quantity = models.ForeignKey(MeasurementQuantity, on_delete=models.CASCADE)


class Collection(models.Model):
    subject = models.CharField(max_length=300, blank=True)
    owner = models.CharField(max_length=300, blank=True)
    note = models.TextField(blank=True)
    created_by = models.ForeignKey(User,
                                   related_name="collections", blank=True, null=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)


class CollectionTitle(models.Model):
    collection = models.ForeignKey(Collection,
                                   related_name="has_titles", on_delete=models.CASCADE)
    name = models.CharField(max_length=500, verbose_name="Title")
    language = models.CharField(max_length=3)
