from django.urls import path
from .views import *

app_name = 'whatscooking'

urlpatterns = [
    path('',  HomeView.as_view(), name='whatscooking-home'),
    path('recipes/', RecipeList.as_view(),
         name='recipe-home'),
    path('recipe/<int:pk>/', RecipeDetail.as_view(),
         name='recipe-detail'),
    path('recipe/create/', RecipeCreate.as_view(),
         name='recipe-create'),
    path('recipe/update/<int:pk>/',
         RecipeUpdate.as_view(), name='recipe-update'),
    path('recipe/delete/<int:pk>/',
         RecipeDelete.as_view(), name='recipe-delete'),
]
