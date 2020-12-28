from django.shortcuts import render

# Create your views here.

def home(request):
    """ A view to return the index page """

    return render(request, 'webpages/index.html')

def our_story(request):
    """ A view to return the our story page """

    return render(request, 'webpages/our_story.html')

def faqs(request):
    """ A view to return the our faqs page """

    return render(request, 'webpages/faqs.html')

def contact_us(request):
    """ A view to return the our contact us page """

    return render(request, 'webpages/contact_us.html')
