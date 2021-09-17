from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class MeasurementUnits(models.Model):
    unit = models.CharField(max_length=100)


class MeasurementQuantity(models.Model):
    quantity = models.CharField(max_length=100)


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    cook_time = models.CharField(max_length=20, null=True)
    serving_size = models.CharField(max_length=20, null=True)
    description = models.TextField()
    directions = models.TextField(null=True)
    date_created = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class PantryIngredients(models.Model):
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class RecipeIngredients(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit_id = models.ForeignKey(MeasurementUnits, on_delete=models.CASCADE)
    quantity_id = models.ForeignKey(
        MeasurementQuantity, on_delete=models.CASCADE)
