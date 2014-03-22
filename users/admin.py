from django.contrib import admin

# Register your models here.
from users.models import Profile, TravelHistory, CriminalHistory

admin.site.register(Profile)
admin.site.register(TravelHistory)
admin.site.register(CriminalHistory)