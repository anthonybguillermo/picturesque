from django.shortcuts import render, get_object_or_404
from .models import Poster

# Create your views here.

def all_posters(request):
    """ A view to show all posters, including sorting and search queries """

    posters = Poster.objects.all()

    context = {
        'posters': posters,
    }

    return render(request, 'posters/posters.html', context)


def poster_detail(request, poster_id):
    """ A view to show individual poster details """

    poster = get_object_or_404(Poster, pk=poster_id)

    context = {
        'poster': poster,
    }

    return render(request, 'posters/poster_detail.html', context)