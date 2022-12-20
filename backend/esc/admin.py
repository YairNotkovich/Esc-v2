from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(User_Role)
admin.site.register(Country)
admin.site.register(Airline_Company)
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(FlightRoute)
admin.site.register(Booking)
