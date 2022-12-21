from ast import Str
import json
import pandas as pd
import numpy as np


def airports_csv_to_json(path_to_csv: Str = r"mockup data/airports.csv"):
    columns = [
        # "id", #0
        "ident",  # 1
        "type",  # 2
        "name",  # 3
        "latitude_deg",  # 4
        "longitude_deg",  # 5
        # "elevation_ft", #6
        # "continent", #7
        "iso_country",  # 8
        # "iso_region", #9
        "municipality",  # 10
        # "scheduled_service", # 11
        # "gps_code", # 12
        "iata_code",  # 13
        # "local_code",  # 14
        # "home_link", # 15
        # "wikipedia_link", # 16
        # "keywords", # 17
    ]

    raw_data = pd.read_csv(path_to_csv, header=0, usecols=[1, 2, 3, 4, 5, 8, 10, 13])

    raw_df = pd.DataFrame(raw_data)
    print(raw_df)
    df = raw_df.loc[
        raw_df["type"].isin(
            [
                "large_airport",
            ]
        )
    ]

    df.to_json(r"mockup data/airports.json", orient="records")


airports_csv_to_json()
