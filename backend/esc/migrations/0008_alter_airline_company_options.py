# Generated by Django 4.1.4 on 2022-12-23 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("esc", "0007_alter_flightroute_distance_alter_flightroute_ident"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="airline_company",
            options={"verbose_name": "Airline"},
        ),
    ]