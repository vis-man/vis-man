from django.contrib import admin
from .models import Site, Visitor, History

class AdminArea(admin.AdminSite):
  site_header = 'UWA Visitor Management System'
  index_title = 'Admin Dashboard'
  site_title = 'UWA VMS'
  

vms_admin = AdminArea(name='vms_admin ')

class HistoryInline(admin.TabularInline):
  model = History

@admin.register(Site, site=vms_admin)
class SiteAdmin(admin.ModelAdmin):
  fieldsets = (
    ("Site Details", {'fields': (('name','accomodation'),)}),
  )

  list_display = ['name','accomodation']
  list_filter = ('accomodation',)

@admin.register(Visitor, site=vms_admin)
class VisitorAdmin(admin.ModelAdmin):
  fieldsets = (
    ("Visitor's Contact Information",{
      'fields':(('first_name','last_name'),('email','phone_number'),'role')
    }),
    ("Visitation Details",{
      'fields':('planned_checkout','checkout','nightstay')
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
    'emergency_relation'
  ]
  readonly_fields = ['checkin']
  list_filter = ('role', 'checkout', 'nightstay')
  inlines = [HistoryInline]

  def visitor_name(self, obj):
    return obj.first_name + ' ' + obj.last_name

  def emergency_name(self, obj):
    if obj.emergency_first_name and obj.emergency_last_name:
      return obj.emergency_first_name + ' ' + obj.emergency_last_name
    else:
      return '-'

@admin.register(History, site=vms_admin)
class HistoryAdmin(admin.ModelAdmin):
  list_display = ['visitor', 'checkin', 'checkout', 'nightstay']
  list_display_links = ['visitor']
  readonly_fields = ['checkin','checkout','nightstay']
  list_filter = ('nightstay',)
  