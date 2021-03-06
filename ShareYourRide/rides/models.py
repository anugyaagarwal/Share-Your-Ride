from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class UserProfile (models.Model):
    user  = models.OneToOneField(User)
    phone_num = models.TextField(blank=True)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __unicode__(self):
        return self.user.username
    
class Address(models.Model):
    add_address = models.TextField(max_length=140,blank=True)
    def __unicode__(self):
        return self.add_address
    
class Ride(models.Model):
    
    CHOICES = (
        ('None','None'),
        ('anytime','anytime'),
        ('early','early (12a-8a)'),
        ('morning','morning (8a-12p)'),
        ('afternoon','afternoon (12p-5p)'),
        ('evening','evening (5p-9p)'),
        ('night','night (9p-12a)')
    )    
    type = models.BooleanField(default=False)
    add_source = models.ForeignKey(Address, related_name='source')
    add_destination = models.ForeignKey(Address, related_name='destination')
    ride_startDateTime = models.DateTimeField(default= datetime.datetime.now, blank=True)
    ride_startPref = models.CharField(max_length=10, choices=CHOICES, default='None')
    ride_returnDateTime = models.DateTimeField(default= datetime.datetime.now, blank=True)
    ride_returnPref = models.CharField(max_length=10, choices=CHOICES, default='None') 
    ride_comment = models.TextField(null=True,max_length=140,blank=True)
    def __unicode__(self):
        return self.ride_comment
    
class Driver(models.Model):
    ride_id = models.ForeignKey(Ride)
    user_id = models.ForeignKey(User)
    drv_carseats = models.SmallIntegerField(null=True,blank=False)
    def __unicode__(self):
        return self.user_id.username
    
class Rider(models.Model):
    ride_id = models.ForeignKey(Ride)
    user_id = models.ForeignKey(User)
    def __unicode__(self):
        return self.user_id.username
    