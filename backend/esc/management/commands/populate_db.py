from django.core.management.base import BaseCommand

# define customized model for use as User
import populate_airports, populate_countries, populate_human, populate_roles


class Command(BaseCommand):
    args = "none"
    help = """
        this script is used to populate the database with data for User_Role
            """

    def handle(self, *args, **options):
        populate_roles.Command().handle()
        populate_human.Command().handle()
        populate_countries.Command().handle()
        populate_airports.Command().handle()
