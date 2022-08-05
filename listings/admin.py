from django.contrib import admin

# Register your models here.
# Listing is the class name of the models.py
from .models import Listing
# create a class for the table by passing tuple
# list display is how data display
# list _display_links create a Link selection
# filter is the filter box at the right
# list_editable for check selection, a save button will generated
# search_fields = create a search box at the top
# list_per_page ; otherwise, the list can keep going without pagation

class ListingAdmin(admin.ModelAdmin):
    List_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    List_display_links = ('id', 'title')
    List_filter = ('realtor')
    List_editable = ('is_published',)
    search_fields = ('title', 'desciption', 'address', 'city', 'state', 'zipcode', 'price',)
    List_per_page = 25

admin.site.register(Listing, ListingAdmin)