from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Site, Visitor, History
from django.http import HttpResponse
import csv

# Django Admin Customizations
admin.site.site_header = 'UWA Visitor Management System'
admin.site.index_title = 'Admin Dashboard'
admin.site.site_title = 'UWA VMS'
admin.site.unregister(Group)
admin.site.unregister(User)

# Django Admin Model Registerations and Customizations
@admin.register(User)
class UserAdmin(BaseUserAdmin):
  def export_as_csv(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)
    writer.writerow(field_names)
    for obj in queryset:
      writer.writerow([getattr(obj, field) for field in field_names])
    return response
  export_as_csv.short_description = "Export Selected"

  actions = ["export_as_csv"]

  list_display = [
      'username',
      'first_name',
      'last_name',
      'email',
      'is_superuser',
      'is_active',
      'is_staff',
      'last_login'
  ]

  fieldsets = (
    ("User Details",{
      'fields':(('first_name','last_name'),('email', 'username'),'last_login', 'date_joined')
    }),
    ("Permissions",{
      'fields':('user_permissions','is_superuser', 'is_staff', 'is_active')
    })
  )

  add_fieldsets = (
    ('User Details', {
      'classes': ('wide',),
      'fields': ('first_name', 'last_name','email',)}
    ),
    ('Permissions', {
      'classes': ('wide',),
      'fields': ('user_permissions','is_superuser', 'is_staff', 'is_active')}
    ),
    ('Login Details - Required', {
      'classes': ('wide',),
      'fields': ('username','password1', 'password2')}
    ),
  )

  readonly_fields = ['last_login', 'date_joined']
  list_filter = ('last_login', 'is_superuser', 'is_staff', 'is_active',)
  search_fields =["username", "first_name", "last_name", 'email']

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
  # defining a django action function to export visitor data to a csv file
  def export_as_csv(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)
    writer.writerow(field_names)
    for obj in queryset:
      writer.writerow([getattr(obj, field) for field in field_names])
    return response
  export_as_csv.short_description = "Export Selected"

  actions = ["export_as_csv"]
  
  fieldsets = (
    ("Site Details", {'fields': (('name','accomodation'),)}
    ),
  )
  
  list_display = ['name','accomodation']
  list_filter = ('accomodation',)

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
  # defining a django action function to export visitor data to a csv file
  def export_as_csv(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)
    writer.writerow(field_names)
    for obj in queryset:
      writer.writerow([getattr(obj, field) for field in field_names])
    return response
  export_as_csv.short_description = "Export Selected"

  # Combines first and last name to make a fullname
  def visitor_name(self, obj):
    return obj.first_name + ' ' + obj.last_name
  # Combines first and last name to make a fullname. If no entry return -
  def emergency_name(self, obj):
    if obj.emergency_first_name and obj.emergency_last_name:
      return obj.emergency_first_name + ' ' + obj.emergency_last_name
    else:
      return '-'

  actions = ["export_as_csv"]

  fieldsets = (
    ("Visitor's Contact Information",{
      'fields':(('first_name','last_name'),('email','phone_number'),'role')
    }),
    ("Visitation Status",{
      'fields':('checkin','planned_checkout','checkout','nightstay', 'site')
    }),
    ("Visitor's Emergency Contact Information",{
      'fields':(('emergency_first_name','emergency_last_name'),('emergency_phone','emergency_relation'))
    }),
  )

  list_display = [
    'visitor_name',
    'role',
    'email',
    'phone_number',
    'checkin',
    'planned_checkout',
    'checkout',
    'nightstay',
    'emergency_name',
    'emergency_phone',
    'emergency_relation',
    'site'
  ]

  list_filter = ('site','checkout', 'checkin', 'planned_checkout', 'role','nightstay',)
  search_fields =["first_name", "last_name", "email"]
  readonly_fields = ['checkin', 'checkout']
  ordering = ('-checkin',)

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
  # defining a django action function to export history data to a csv file
  def export_as_csv(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)
    writer.writerow(field_names)
    for obj in queryset:
      writer.writerow([getattr(obj, field) for field in field_names])
    return response
  export_as_csv.short_description = "Export Selected"

  actions = ["export_as_csv"]

  list_display = ['visitor', 'checkin', 'checkout', 'nightstay', 'site']
  list_display_links = ['visitor']
  list_filter = ('site','checkin', 'checkout','nightstay',)
  search_fields =["visitor__first_name", "visitor__last_name"]
  readonly_fields = ['site', 'visitor', 'checkin','checkout','nightstay']
  ordering = ('-checkout',)