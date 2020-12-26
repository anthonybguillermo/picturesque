from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Poster, Category

# Create your views here.

def all_posters(request):
    """ A view to show all posters, including sorting and search queries """

    posters = Poster.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            posters = posters.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria was entered!")
                return redirect(reverse('posters'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            posters = posters.filter(queries)

    context = {
        'posters': posters,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'posters/posters.html', context)


def poster_detail(request, poster_id):
    """ A view to show individual poster details """

    poster = get_object_or_404(Poster, pk=poster_id)

    context = {
        'poster': poster,
    }

    return render(request, 'posters/poster_detail.html', context)