from esc.models import FlightRoute, Airport, Airline_Company
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

import json

# from flight_app.utils.db_utils import dataManageUtils as dm
from geopy import distance as D

jsonPath = "mockup data/flight_routes.json"


class Command(BaseCommand):
    def insert_data(self):

        try:
            with open(jsonPath, "r", encoding="utf8") as data:
                raw_list = json.load(data)
        except Exception as e:
            print(e)
            return None

        for route in raw_list:
            try:
                airline = Airline_Company.objects.get(code__iexact=route["airline"])

                origin = Airport.objects.filter(iata_code__iexact=route["origin"])[0]
                destination = Airport.objects.filter(iata_code__iexact=route["target"])[
                    0
                ]

                origin_lat_lon = (origin.lat_decimal, origin.lon_decimal)
                dest_lat_lon = (destination.lat_decimal, destination.lon_decimal)
                distance = D.geodesic(origin_lat_lon, dest_lat_lon).km

                FlightRoute.objects.get_or_create(
                    airline=airline,
                    origin=origin,
                    destination=destination,
                    # distance=distance,
                )

            except Exception as e:
                print(
                    e,
                )

    def handle(self, *args, **options):
        self.insert_data()
