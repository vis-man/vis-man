from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
import uuid

class Visitor(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  first_name = models.CharField(max_length=50, null=False, blank=False)
  last_name = models.CharField(max_length=50, null=False, blank=False)
  email = models.EmailField(max_length=200, null=False, blank=False, unique=True)
  phone_number = PhoneNumberField(unique=True, null=False, blank=False, region='AU')
  role = models.CharField(max_length=100, null=False, blank=False)
  nightstay = models.BooleanField(default=False)
  checkin = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), editable=False)
  planned_checkout = models.DateTimeField(null=False, blank=False)
  checkout = models.BooleanField(default=False, null=True, blank=True)
  emergency_first_name = models.CharField(max_length=50, null=True, blank=True)
  emergency_last_name = models.CharField(max_length=50, null=True, blank=True)
  emergency_phone = PhoneNumberField(unique=True, null=True, blank=True, region='AU')
  emergency_relation = models.CharField(max_length=50, null=True, blank=True)
  
  def __str__(self):
    return self.first_name + ' ' + self.last_name

class Site(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  name = models.CharField(max_length=100, unique=True)
  accomodation = models.BooleanField(default=False)
  visitor = models.ManyToManyField(Visitor)

  def __str__(self):
    return self.name

class History(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  checkin = models.DateTimeField(null=False, blank=False, editable=False)
  checkout = models.DateTimeField(null=False, blank=False, editable=False)
  nightstay = models.BooleanField(null=False, blank=False, editable=False)
  visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.checkin