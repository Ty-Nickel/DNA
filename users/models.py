from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class Profile(AbstractUser):

    age = models.IntegerField(max_length=6, null=True, blank=True)
    gender = models.CharField(max_length=8, null=True, blank=True)
    street_number = models.IntegerField(max_length=60, null=True, blank=True)
    street_name = models.CharField(max_length=60, null=True, blank=True)
    unit_number = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=8, null=True, blank=True)
    zip = models.IntegerField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self):
        return self.username


class TravelHistory(models.Model):
    user = models.ForeignKey('Profile')

    airport = models.CharField(max_length=30, null=True, blank=True)
    airline = models.CharField(max_length=30, null=True, blank=True)
    travel_date = models.DateField(null=True, blank=True)


class CriminalHistory(models.Model):
    user = models.ForeignKey('Profile')

    crime = models.CharField(max_length=30, null=True, blank=True)
    charge = models.CharField(max_length=15, null=True, blank=True)
    date = models.DateField(null=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    verdict = models.CharField(max_length=10, null=True, blank=True)







