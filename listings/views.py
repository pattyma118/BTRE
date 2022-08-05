from django.shortcuts import get_object_or_404, render
# import the 404 as well
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# choices at the same folder
from .choices import price_choices, state_choices, bedroom_choices
# load database into view
from .models import Listing


def index(request):
    return render(request, 'listings/listings.html')

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')