from django.db import models
from geo.models import Airline_Company, FlattenedFlightRoutes
from users.models import UserProfile
from datetime import datetime


class Customer(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)


class Supplier(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)


class Flight(models.Model):

    flight_route = models.ForeignKey(
        FlattenedFlightRoutes, on_delete=models.CASCADE, blank=True
    )

    airline = models.ForeignKey(Airline_Company, on_delete=models.CASCADE, blank=True)
    depart_sched = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    duration = models.IntegerField(blank=True, verbose_name="minutes of flight")
    arrive_calculated = models.DateTimeField(null=True, blank=True)
    flight_number = models.CharField(max_length=20, blank=True)
    available_tickets = models.IntegerField(default=380, blank=True)
    flight_range = models.IntegerField(default=0, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.flight_number)

    def save(self, *args, **kwargs):
        # made up speed to calculate duration
        average_speed = 650
        self.flight_range = self.flight_route.distance
        self.duration = self.flight_route.distance * 60 / average_speed
        self.arrive_calculated = self.depart_sched + datetime.timedelta(
            minutes=self.duration
        )
        self.flight_number = (
            self.airline.code + self.flight_route.code + str(self.depart_sched.date)
        )
        return super().save(*args, **kwargs)


class Booking(models.Model):
    flight = models.ManyToManyField(Flight)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    passengers = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}, {self.flight}, {self.customer}"
