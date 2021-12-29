from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import URLValidator


class Recipe(models.Model):
    image = models.ImageField(
        default='default_recipe.png', upload_to='recipe_pics')
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    cook_time = models.CharField(max_length=20, null=True, blank=True)
    serving_size = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(
        validators=[URLValidator()], null=True, blank=True, max_length=100)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})


class Ingredient(models.Model):
    image = models.ImageField(
        default='default_ingredient.png', upload_to='ingredient_pics')
    name = models.CharField(max_length=300)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('ingredient-detail', kwargs={'pk': self.pk})


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)


class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe,
                               related_name="has_steps", on_delete=models.CASCADE)
    description = models.TextField()
    order = models.IntegerField()
