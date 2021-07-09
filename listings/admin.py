from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'branch', 'category', 'make', 'model', 'city', 'postcode', 'is_published',
                    'price', 'salesexecutive')
    list_display_links = ('id', 'branch')
    list_filter = ('salesexecutive',)
    list_editable = ('is_published',)
    search_fields = ('branch', 'description', 'make', 'model',
                     'postcode', 'address', 'city')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
