from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import *


class AirlineSerializer(ModelSerializer):
    class Meta:
        model = Airline_Company
        fields = "__all__"
