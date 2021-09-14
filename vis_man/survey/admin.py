from django.contrib import admin
from .models import Site, Visitor, History

## Changes the way these are displayed on the admin app, can be sorted by these lists
@admin.register(Site)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','accomodation')

@admin.register(Visitor)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")

@admin.register(History)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('visitor',"checkin", 'checkout', 'nightstay')
    
# admin.site.register(Site)
# admin.site.register(Visitor)
# admin.site.register(History)

