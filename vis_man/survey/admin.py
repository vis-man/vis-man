from django.contrib import admin
from .models import Site, Visitor, History

# @admin.register(Site)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = 

@admin.register(Visitor)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")

@admin.register(History)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('visitor',"checkin", 'checkout', 'nightstay')

# admin.site.register(Site)
# admin.site.register(Visitor)
# admin.site.register(History)

