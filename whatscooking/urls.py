from django.urls import path
from whatscooking import views
from .views import *


app_name = 'whatscooking'

urlpatterns = [
    path('',  HomeView.as_view(), name='whatscooking-home'),
    # -----------------------------------------------------
    path('recipes/', RecipeListView.as_view(),
         name='recipe-home'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(),
         name='recipe-detail'),
    path('recipe/create/', RecipeCreate.as_view(),
         name='recipe-create'),
    path('recipe/update/<int:pk>/',
         RecipeUpdate.as_view(), name='recipe-update'),
    path('recipe/delete/<int:pk>/',
         RecipeDeleteView.as_view(), name='recipe-delete'),
    # -----------------------------------------------------
    path('ingredients/',  IngredientListView.as_view(), name='ingredient-home'),
    path('ingredient/<int:pk>/', IngredientDetailView.as_view(),
         name='ingredient-detail'),
    path('ingredient/new/', IngredientCreateView.as_view(),
         name='ingredient-create'),
    path('ingredient/<int:pk>/update/',
         IngredientUpdateView.as_view(extra_context={'img_p': 'true'}), name='ingredient-update'),
    path('ingredient/<int:pk>/delete/',
         IngredientDeleteView.as_view(), name='ingredient-delete'),
     # -----------------------------------------------------
    path('measurement/',  MeasurementListView.as_view(), name='measurement-home'),
]
