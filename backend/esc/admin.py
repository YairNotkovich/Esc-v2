from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'role','contact_display','phone_display', 'avatar')

    @admin.display(ordering='user')
    def display_name(self, obj):
        return obj.user.last_name + " " + obj.user.first_name

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(User_Role)
# admin.site.register(Country)
# admin.site.register(Airline_Company)
# admin.site.register(Airport)
# admin.site.register(Flight)
# admin.site.register(FlightRoute)
# admin.site.register(FlattenedFlightRoutes)
# admin.site.register(Booking)
