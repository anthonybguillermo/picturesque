from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    frame = None
    bag = request.session.get('bag', {})
    if 'poster_size' in request.POST:
        frame = request.POST['poster_frame']
    bag = request.session.get('bag', {})

    if frame:
        if item_id in list(bag.keys()):
            if frame in bag[item_id]['items_by_frame'].keys():
                bag[item_id]['items_by_frame'][frame] += quantity
            else:
                bag[item_id]['items_by_frame'][frame] = quantity
        else:
            bag[item_id] = {'items_by_frame': {frame: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
