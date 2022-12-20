from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from esc.management.commands import populate_roles
import json
from esc.models import UserProfile, User_Role

# define customized model for use as User
User = get_user_model()
jsonPath = "mockup data/users.json"


class Command(BaseCommand):
    args = "none"
    help = """
        this script is used to populate the database with data for users and user profiles
            """

    def insert_data(self):
        try:
            User.objects.create_superuser("yair", "yair.notkovich@gmail.com", "wbstbh")
        except:
            pass

        try:
            with open(jsonPath, "r", encoding="utf8") as data:
                raw_list = json.load(data)
        except Exception as e:
            print(e)
            return None

        for i, user in enumerate(raw_list):

            """
            standard Django USER Fields
            id, password, username, first_name, last_name
            email, is_staff, is_active, is_superuser
            """

            new_user = User.objects.get_or_create(
                username=user["username"],
                password="123a456b",
                first_name=user["first_name"],
                last_name=user["last_name"],
                email=user["email"],
            )

            profile = UserProfile.objects.get(
                user=User.objects.get(username=user["username"])
            )
            profile.avatar = user["picture"]
            profile.phone_no = user["phone_number"]
            id = lambda x: 3 if x % 4 == 0 else 2
            profile.role = User_Role.objects.get(id=id(i))
            profile.save()

    def handle(self, *args, **options):
        populate_roles.Command().handle()
        self.insert_data()
