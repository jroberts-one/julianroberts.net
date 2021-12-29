from django.contrib import admin
from .models import Recipe, RecipeStep, Ingredient

admin.site.register(Recipe)
admin.site.register(RecipeStep)
admin.site.register(Ingredient)
