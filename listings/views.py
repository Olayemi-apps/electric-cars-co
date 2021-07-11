from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import doors_choices, price_choices, branch_choices

from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Check for keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # Check for city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)

    # Check for branch
    if 'branch' in request.GET:
        branch = request.GET['branch']
        if branch:
            queryset_list = queryset_list.filter(
                branch__iexact=branch)

    # Check for amount of car doors
    if 'doors' in request.GET:
        doors = request.GET['doors']
        if doors:
            queryset_list = queryset_list.filter(
                doors__lte=doors)

    # Check for price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)  # Used lte = less than or equal to in the search option

    context = {
        'doors_choices': doors_choices,
        'price_choices': price_choices,
        'branch_choices': branch_choices,
        'listings': queryset_list,
        # values - then add "values.keywords" to the html lets the content searched for stay within the textfield
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)
