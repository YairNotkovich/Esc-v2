from django.contrib import admin
from .models import User, UserProfile, User_Role


# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(User_Role)
