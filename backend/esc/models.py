from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# custom User model to allow email sign instead of user


class User(AbstractUser):
    email = models.EmailField("user email", max_length=240, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        # "username",
    ]

    def __str__(self):
        return str(self.email)


class User_Role(models.Model):
    role_name = models.CharField(max_length=15, unique=True)

    def __str__(self) -> str:
        return self.role_name


class UserProfile(models.Model):
    def contact_default():
        return {
            "phone number": "",
            "address": {
                "street": "",
                "city": "",
                "state": "",
                "postcode": "",
            },
        }

    def favorites_default():
        return {}

    def booking_default():
        return {}

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.ForeignKey(
        User_Role, on_delete=models.CASCADE, default=1, null=True, verbose_name="Role"
    )
    avatar = models.ImageField("Avatar", upload_to="avatars", null=True)
    contact_info = models.JSONField("Contact Info", default=contact_default)
    favorite = models.JSONField("Favorites", default=favorites_default)
    booking = models.JSONField("Bookings", default=booking_default)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        verbose_name = "Profile"


class Country(models.Model):
    code = models.CharField("IATA Code", max_length=2, unique=True)
    name = models.CharField("Name", max_length=20, unique=True)
    flag = models.CharField("Flag URL", max_length=200, null=True)

    class Meta:
        verbose_name = "Country"

    def __str__(self):
        return self.name


class Airline_Company(models.Model):
    code = models.CharField("IATA Code", max_length=2, unique=True)
    name = models.CharField("Airline Name", max_length=100, null=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, verbose_name="Base Country", default=1
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name="Manager ID"
    )
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name, self.code


class Airport(models.Model):

    icao_code = models.CharField(max_length=4)
    iata_code = models.CharField(max_length=3)
    display_name = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)
    country_name = models.CharField(max_length=20)
    lat_decimal = models.FloatField()
    lon_decimal = models.FloatField()

    def save(self, *args, **kwargs):
        self.country_name = Country.objects.get(id=self.country_id).name
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Airport"

    def __str__(self):
        return f"{self.iata_code}|{self.country_name}|{self.city}"


class FlightRoute(models.Model):
    airline = models.ForeignKey(Airline_Company, on_delete=models.CASCADE, null=False)
    origin = models.ForeignKey(
        Airport, on_delete=models.CASCADE, null=False, related_name="Origin_Airport"
    )
    destination = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE,
        null=False,
        related_name="Destination_Airport",
    )
    distance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.airline.Code} from: {self.origin}  to: {self.destination}  distance:{self.distance}"


class Flight(models.Model):
    airline_company_id = models.ForeignKey(Airline_Company, on_delete=models.CASCADE)
    # Origin_Country_Id = models.ForeignKey(
    #     Country, null=False, on_delete=models.CASCADE, related_name='Origin_Country_Id')
    # Destination_Country_Id = models.ForeignKey(
    #     Country, null=False, on_delete=models.CASCADE, related_name='Destination_Country_Id')
    origin_airport = models.ForeignKey(
        Airport, null=False, on_delete=models.CASCADE, related_name="Origin_airport_Id"
    )
    destination_airport = models.ForeignKey(
        Airport,
        null=False,
        on_delete=models.CASCADE,
        related_name="Destination_airport_Id",
    )
    departure_time = models.DateTimeField(null=True)
    landing_time = models.DateTimeField(null=True)
    flight_number = models.CharField(max_length=20)
    available_tickets = models.IntegerField(default=100)
    flight_range = models.IntegerField(default=0)


class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    seats = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.pk}, {self.Flight}, {self.Customer}"
