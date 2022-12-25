from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
from esc.models import Customer

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'role','contact_display','phone_display', 'avatar')
    fetch_related = ('customer')
    @admin.display(ordering='user')
    def display_name(self, obj):
        return obj.user.last_name + " " + obj.user.first_name

    # @admin.display()
    # def bookings(self, obj):
    #     customer = Customer.objects.get(user = obj)
    #     bookings = customer.booking_set.all()
    #     # print(customer)
    #     # return bookings.id
    #     return "%s"% (" ".join(booking.flight for booking in bookings))

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(User_Role)