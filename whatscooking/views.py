from django.shortcuts import render
from .models import Recipe

def home(request):
    context = {
        'title': 'whatscooking',
        'recipes': Recipe.objects.all()
    }
    return render(request, 'whatscooking/home.html', context)

