from django.db import models
from datetime import datetime
import uuid
from django.core.exceptions import ValidationError

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
    def validate_phone(value):
        allowed = '0123456789(+) -'
        for character in value:
            if str(character) not in allowed:
                raise ValidationError('Invalid phone number provided.')
            elif len(value) < 8 or len(value) > 20:
                raise ValidationError('Phone number must be 8-20 characters long.')

    def validate_name(value):
        for character in value:
            if (str(character).isalpha() is False) and (str(character) != '.' and str(character) != ' '): 
                raise ValidationError('Name must only contain alphabets.')

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    first_name = models.CharField(max_length=50, null=False, blank=False, validators=[validate_name])
    last_name = models.CharField(max_length=50, null=False, blank=False, validators=[validate_name])
    email = models.EmailField(max_length=200, null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False, validators=[validate_phone])
    role = models.CharField(max_length=50, null=False, blank=False)
    nightstay = models.BooleanField(default=False)
    checkin = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), editable=False)
    planned_checkout = models.DateTimeField(null=False, blank=False)
    # Stores which site visitor is currently checked in. If visitor is checked out,
    # it stores their last visited site.
    site = models.ForeignKey(Site, blank=True, null=True, on_delete=models.CASCADE)
    # If visitor is currently in the building, checkout is false. If they sign out,
    # checkout is true.
    checkout = models.BooleanField(default=False)
    emergency_first_name = models.CharField(max_length=50, null=True, blank=True, validators=[validate_name])
    emergency_last_name = models.CharField(max_length=50, null=True, blank=True, validators=[validate_name])
    emergency_phone = models.CharField(max_length=16, null=True, blank=True, validators=[validate_phone])
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
