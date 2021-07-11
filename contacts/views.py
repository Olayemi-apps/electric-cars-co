from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        salesexecutive_email = request.POST['salesexecutive_email']

        # Check user user has a previous enquiry pending

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)

            if has_contacted:
                messages.error(
                    request, 'You have already made an enquiry for this car')
                return redirect('/listings/'+listing_id)

    contact = Contact(listing=listing, listing_id=listing_id, name=name,
                      email=email, phone=phone, message=message, user_id=user_id)

    contact.save()

    messages.success(
        request, 'Thank you for you enquiry, One of our Sales Executives will get back to you as soon as possible')
    return redirect('/listings/'+listing_id)
