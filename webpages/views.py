from django.shortcuts import render

# Create your views here.

def home(request):
    """ A view to return the index page """

    return render(request, 'index.html')
