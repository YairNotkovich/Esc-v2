import requests
from django.core.management.base import BaseCommand
from esc.models import Country, Airport
import json

# define customized model for use as User

jsonPath = "mockup data/airports.json"

# json structure
# {
#     "ident": "AGGH",
#     "type": "large_airport",
#     "name": "Honiara International Airport",
#     "latitude_deg": -9.428,
#     "longitude_deg": 160.054993,
#     "iso_country": "SB",
#     "municipality": "Honiara",
#     "iata_code": "HIR",
# }


class Command(BaseCommand):
    args = "none"
    help = """
        this script is used to populate the database with data for User_Role
            """

    def insert_data(self):

        try:
            with open(jsonPath, "r", encoding="utf8") as data:
                raw_list = json.load(data)
        except Exception as e:
            print(e)
            return None

        for airport in raw_list:

            try:
                Airport.objects.get_or_create(
                    icao_code=airport["ident"],
                    iata_code=airport["iata_code"],
                    name=airport["name"],
                    country=Country.objects.get(code=airport["iso_country"]),
                    city=airport["municipality"],
                    lat_decimal=airport["latitude_deg"],
                    lon_decimal=airport["longitude_deg"],
                )
            except Exception as e:
                print(e, airport)

    def handle(self, *args, **options):
        self.insert_data()
