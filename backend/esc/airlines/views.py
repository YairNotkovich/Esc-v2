from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from esc.models import Flight, User, Airline_Company, User_Role, Airport, UserProfile
from esc.serializers import AirlineSerializer
from django.contrib.auth.decorators import user_passes_test
from rest_framework import status

# Create your views here.
MODEL_SERIALIZER = AirlineSerializer
MODEL = MODEL_SERIALIZER.Meta.model


@api_view(["GET"])
def airline_list(request):

    # get all objects in the model airline_companies
    result = MODEL.objects.all()
    serialized = MODEL_SERIALIZER(result, many=True)
    return Response(serialized.data)


@api_view(["GET"])
def airline_routes():
    pass
