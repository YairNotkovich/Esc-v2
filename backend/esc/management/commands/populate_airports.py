import requests
from django.core.management.base import BaseCommand
from esc.models import Country, Airport
import json

# define customized model for use as User

jsonPath = "mockup data/osm-world-airports.json"


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
            Airport.objects.get_or_create()

    def handle(self, *args, **options):
        self.insert_data()
