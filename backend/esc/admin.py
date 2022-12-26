from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *



class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user','bookings')

    @admin.display()
    def bookings(self, obj):
        bookings = obj.booking_set.all()
        # print(customer)
        # return bookings.id
        return "%s"% (" ".join(booking.flight for booking in bookings))

# admin.site.register(User, UserAdmin)
# admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Customer,CustomerAdmin)
# admin.site.register(Country)
# admin.site.register(Airline_Company)
# admin.site.register(Airport)
admin.site.register(Flight)
# admin.site.register(FlightRoute)
# admin.site.register(FlattenedFlightRoutes)
admin.site.register(Booking)
