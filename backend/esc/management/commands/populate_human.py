from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from esc.management.commands import populate_roles

# define customized model for use as User
User = get_user_model()


class Command(BaseCommand):
    args = "none"
    help = """
        this script is used to populate the database with data,
        please uncomment the data you wish to populate in the 'handle' function at the bottom
            """

    def __init__(self):
        populate_roles.Command().handle()
        try:
            User.objects.create_superuser("yair", "yair.notkovich@gmail.com", "wbstbh")
        except:
            pass

    def insert_user(self):
        pass

    def update_user_profile():
        pass

    def handle(self, *args, **options):
        self.insert_user()
