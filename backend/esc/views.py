from queue import Empty
import random
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.contrib.auth import get_user_model


@api_view(["POST", "GET"])
def test(request):

    return Response({}, status=status.HTTP_200_OK)
