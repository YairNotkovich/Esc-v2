from django.core.management.base import BaseCommand
from esc.models import Country, Airline_Company
import json

# define customized model for use as User

jsonPath = "mockup data/airlines.json"

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

        for airline in raw_list:

            try:
                country = Country.objects.get(name__iexact=airline["Country"])

            except Exception as e:
                print(e, country)
                continue
            else:
                Airline_Company.objects.get_or_create(
                    code=airline["IATA"],
                    name=airline["Name"],
                    country=country,
                )

    def handle(self, *args, **options):
        self.insert_data()
