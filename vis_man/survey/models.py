from django.db import models
from datetime import datetime
import uuid

class Site(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  name = models.CharField(max_length=100, unique=True)
  accomodation = models.BooleanField(default=False)

  def __str__(self):
    return self.name

class Visitor(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  first_name = models.CharField(max_length=50, null=False, blank=False)
  last_name = models.CharField(max_length=50, null=False, blank=False)
  email = models.EmailField(max_length=200, null=False, blank=False, unique=True)
  phone_number = models.CharField(max_length=20,null=False, blank=False)
  role = models.CharField(max_length=100, null=False, blank=False)
  nightstay = models.BooleanField(default=False)
  checkin = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), editable=False)
  planned_checkout = models.DateTimeField(null=False, blank=False)
  site = models.ForeignKey(Site, blank=True, null=True, on_delete=models.CASCADE)
  checkout = models.BooleanField(default=False)
  emergency_first_name = models.CharField(max_length=50, null=True, blank=True)
  emergency_last_name = models.CharField(max_length=50, null=True, blank=True)
  emergency_phone = models.CharField(max_length=20,null=True, blank=True)
  emergency_relation = models.CharField(max_length=50, null=True, blank=True)

  def __str__(self):
    return self.first_name + ' ' + self.last_name  

class History(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  checkin = models.DateTimeField(null=False, blank=False, editable=False)
  checkout = models.DateTimeField(null=False, blank=False, editable=False)
  site = models.ForeignKey(Site, blank=True, on_delete=models.PROTECT)
  nightstay = models.BooleanField(null=False, blank=False, editable=False)
  visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT)

  class Meta:
    verbose_name_plural = ("Histories")
  
  def __str__(self):
    return str(self.id)