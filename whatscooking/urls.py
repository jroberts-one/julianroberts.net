from django.urls import path
from .views import *
from whatscooking import views

app_name = 'whatscooking'

urlpatterns = [
    path('',  HomeView.as_view(), name='whatscooking-home'),
    path('recipes/',  RecipeListView.as_view(), name='recipe-home'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/update/',
         RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete/',
         RecipeDeleteView.as_view(), name='recipe-delete'),


    path('collections/', CollectionListView.as_view(),
         name='collection_list'),
    path('collection/<int:pk>/', CollectionDetailView.as_view(),
         name='collection_detail'),
    path('collection/create/', CollectionCreate.as_view(),
         name='collection_create'),
    path('collection/update/<int:pk>/',
         CollectionUpdate.as_view(), name='collection_update'),
    path('collection/delete/<int:pk>/',
         CollectionDelete.as_view(), name='collection_delete'),


    path('ingredients/',  IngredientListView.as_view(), name='ingredient-home'),
    path('ingredient/<int:pk>/', IngredientDetailView.as_view(),
         name='ingredient-detail'),
    path('ingredient/new/', IngredientCreateView.as_view(),
         name='ingredient-create'),
    path('ingredient/<int:pk>/update/',
         IngredientUpdateView.as_view(extra_context={'img_p': 'true'}), name='ingredient-update'),
    path('ingredient/<int:pk>/delete/',
         IngredientDeleteView.as_view(), name='ingredient-delete'),

    path('measurement/',  MeasurementListView.as_view(), name='measurement-home'),
]
