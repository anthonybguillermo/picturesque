from django.shortcuts import render
from .models import Poster

# Create your views here.

def all_posters(request):
    """ A view to show all posters, including sorting and search queries """

    posters = Poster.objects.all()

    context = {
        'posters': posters,
    }

    return render(request, 'posters/posters.html', context)