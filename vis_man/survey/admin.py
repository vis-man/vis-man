from django.contrib import admin
from .models import Site, Visitor, History

admin.site.register(Site)
admin.site.register(Visitor)
admin.site.register(History)

