from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
import uuid

'''Site model to store details of each site monitored by VMS'''
class Site(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  name = models.CharField(max_length=100, unique=True)
  accomodation = models.BooleanField(default=False)

  def __str__(self):
    return self.name

'''Visitors are first stored when they check in for the first time. Subsequent
   checkin updates these fields.'''
class Visitor(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  first_name = models.CharField(max_length=50, null=False, blank=False)
  last_name = models.CharField(max_length=50, null=False, blank=False)
  email = models.EmailField(max_length=200, null=False, blank=False, unique=True)
  # Phone number must be Australian (eg. 0423 242 257, or have an international 
  # prefix infront +61 423 242 257)
  phone_number = PhoneNumberField(null=False, blank=False)
  phone_number.error_messages['invalid'] = 'Enter a valid phone number'
  role = models.CharField(max_length=100, null=False, blank=False)
  nightstay = models.BooleanField(default=False)
  checkin = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), editable=False)
  planned_checkout = models.DateTimeField(null=False, blank=False)
  # Stores which site visitor is currently checked in. If visitor is checked out,
  # it stores their last visited site.
  site = models.ForeignKey(Site, blank=True, null=True, on_delete=models.CASCADE)
  # If visitor is currently in the building, checkout is false. If they sign out,
  # checkout is true.
  checkout = models.BooleanField(default=False)
  emergency_first_name = models.CharField(max_length=50, null=True, blank=True)
  emergency_last_name = models.CharField(max_length=50, null=True, blank=True)
  emergency_phone = PhoneNumberField(null=True, blank=True)
  emergency_phone.error_messages['invalid'] = "Enter a valid emergency number"
  emergency_relation = models.CharField(max_length=50, null=True, blank=True)

  def __str__(self):
    return self.first_name + ' ' + self.last_name  

'''Visitors stay details for each visit is logged into this model'''
class History(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  checkin = models.DateTimeField(null=False, blank=False, editable=False)
  checkout = models.DateTimeField(null=False, blank=False, editable=False)
  site = models.ForeignKey(Site, blank=True, on_delete=models.PROTECT)
  nightstay = models.BooleanField(null=False, blank=False, editable=False)
  visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural = ("Histories")
  
  def __str__(self):
    duration = str(self.checkout - self.checkin)
    duration = duration.split(':')
    return "Visit Duration: " + duration[0] + " hours and " + duration[1] + " Minutes"