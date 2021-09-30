from django.contrib import admin
from .models import Site, Visitor, History
from django.http import HttpResponse
import csv

# Customizable Django admin
class AdminArea(admin.AdminSite):
  site_header = 'UWA Visitor Management System'
  index_title = 'Admin Dashboard'
  site_title = 'UWA VMS'
  
vms_admin = AdminArea(name='vms_admin ')

@admin.register(Site, site=vms_admin)
class SiteAdmin(admin.ModelAdmin):
  fieldsets = (
    ("Site Details", {'fields': (('name','accomodation'),)}),
  )
  list_display = ['name','accomodation']
  list_filter = ('accomodation',)

@admin.register(Visitor, site=vms_admin)
class VisitorAdmin(admin.ModelAdmin):
  actions = ["export_as_csv"]
  # defining a django action function to export visitor data to a csv file
  def export_as_csv(self, queryset):
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
  readonly_fields = ['checkin', 'checkout']
  list_filter = ('role', 'checkout', 'nightstay', 'checkin', 'planned_checkout', 'site')

  '''Combines first and last name to make a fullname'''
  def visitor_name(self, obj):
    return obj.first_name + ' ' + obj.last_name
  '''Combines first and last name to make a fullname. If no entry return -'''
  def emergency_name(self, obj):
    if obj.emergency_first_name and obj.emergency_last_name:
      return obj.emergency_first_name + ' ' + obj.emergency_last_name
    else:
      return '-'

@admin.register(History, site=vms_admin)
class HistoryAdmin(admin.ModelAdmin):
  actions = ["export_as_csv"]
  # defining a django action function to export visitor data to a csv file
  def export_as_csv(self, queryset):
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
  list_display = ['visitor', 'checkin', 'checkout', 'nightstay']
  list_display_links = ['visitor']
  readonly_fields = ['site', 'visitor', 'checkin','checkout','nightstay']
  list_filter = ('nightstay',)