from ast import Str
import pandas as pd


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
    df = raw_df.loc[raw_df["type"].isin(["large_airport", "medium_airport"])]

    df.to_json(r"mockup data/airports.json", orient="records")


def airlines_csv_to_json(
    path_to_csv: Str = r"mockup data/airlines.csv",
):

    columns = [
        "id",  # 0
        "Name",  # 1
        "Alias",  # 2
        "IATA",  # 3
        "ICAO",  # 4
        "Callsign",  # 5
        "Country",  # 6
        "Active",  # 7
    ]

    raw_data = pd.read_csv(path_to_csv, names=columns, usecols=[1, 3, 4, 6, 7])
    raw_df = pd.DataFrame(raw_data)
    # print(raw_df)
    raw_df.drop(raw_df[raw_df.Active == "N"].index, inplace=True)
    df = raw_df.dropna()
    # print(raw_df)
    df.to_json(r"mockup data/airlines.json", orient="records")


def flight_route_csv_to_json(path_to_csv: Str = r"mockup data/flightroutes.csv"):
    columns = [
        "airline",  # 0
        # 'na', #1
        "origin",  # 2
        # 'na'  ,    #3
        "target",  # 4
        # 'na' ,  #5
        # 'na' ,  #6
        # 'na' ,  #7
        # 'na' ,   #8
        # 'na' ,   #9
    ]

    raw_data = pd.read_csv(
        path_to_csv,
        header=None,
        skipinitialspace=True,
        names=columns,
        usecols=[0, 2, 4],
    )

    df = pd.DataFrame(raw_data)
    df.to_json(r"mockup data/flight_routes.json", orient="records")


airports_csv_to_json()
# airlines_csv_to_json()
# flight_route_csv_to_json()
