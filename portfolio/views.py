from django.shortcuts import render

# logic for how to handle request when user visits home page
def home(request):
    return render(request, 'portfolio/home.html', {'title': 'home'})

def marathon(request):
    return render(request, 'portfolio/marathon.html', {'title': 'marathon'})
