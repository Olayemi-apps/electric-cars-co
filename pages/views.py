from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import doors_choices, price_choices, branch_choices


from listings.models import Listing
from salesexecutives.models import Salesexecutive


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'doors_choices': doors_choices,
        'price_choices': price_choices,
        'branch_choices': branch_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Sales Executives
    salesexecutives = Salesexecutive.objects.all()

    # Get best salesperson
    best_sales = Salesexecutive.objects.all().filter(best_sales_person=True)

    context = {
        'salesexecutives': salesexecutives,
        'best_sales': best_sales
    }

    return render(request, 'pages/about.html', context)
