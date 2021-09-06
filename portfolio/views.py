from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html', {'title': 'home'})

def marathon(request):
    return render(request, 'portfolio/marathon.html', {'title': 'marathon'})
