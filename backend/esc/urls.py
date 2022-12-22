from django.urls import path, include
from views import *

urlpatterns = [
    path("", test, name="test_ops"),
    path("airlines/", include("esc.airlines.urls"), name="airline_ops"),
]
