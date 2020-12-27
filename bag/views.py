from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from posters.models import Poster

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    poster = get_object_or_404(Poster, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    frame = None
    bag = request.session.get('bag', {})
    if 'poster_frame' in request.POST:
        frame = request.POST['poster_frame']
    bag = request.session.get('bag', {})

    if frame:
        if item_id in list(bag.keys()):
            if frame in bag[item_id]['items_by_frame'].keys():
                bag[item_id]['items_by_frame'][frame] += quantity
                messages.success(request, f'Updated frame {frame.upper()} {frame.name} quantity to {bag[item_id]["items_by_frame"][frame]}')
            else:
                bag[item_id]['items_by_frame'][frame] = quantity
                messages.success(request, f'Added frame {poster.upper()} {poster.name} to your bag')
        else:
            bag[item_id] = {'items_by_frame': {frame: quantity}}
            messages.success(request, f'Added frame {poster.upper()} {poster.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {poster.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {poster.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    poster = get_object_or_404(Poster, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    frame = None
    bag = request.session.get('bag', {})
    if 'poster_frame' in request.POST:
        frame = request.POST['poster_frame']
    bag = request.session.get('bag', {})

    if frame:
        if quantity > 0:
            bag[item_id]['items_by_frame'][frame] = quantity
            messages.success(request, f'Updated frame {frame.upper()} {frame.name} quantity to {bag[item_id]["items_by_frame"][frame]}')
        else:
            del bag[item_id]['items_by_frame'][frame]
            if not bag[item_id]['items_by_frame']:
                bag.pop(item_id)
            messages.success(request, f'Removed frame {poster.upper()} {poster.name} from your bag') 
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {poster.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {poster.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    try:
        poster = get_object_or_404(Poster, pk=item_id)
        frame = None
        if 'poster_frame' in request.POST:
            frame = request.POST['poster_frame']
        bag = request.session.get('bag', {})

        if frame:
            del bag[item_id]['items_by_frame'][frame]
            if not bag[item_id]['items_by_frame']:
                bag.pop(item_id)
            messages.success(request, f'Removed frame {poster.upper()} {poster.name} from your bag')
        else:     
            bag.pop(item_id)
            messages.success(request, f'Removed {poster.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
