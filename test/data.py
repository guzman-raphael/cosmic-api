# docker run --rm -itv /home/raphael/Documents/github/cosmic-api/test:/tmp/test --workdir /tmp/test python:slim bash
import json
from faker import Faker
from faker.providers.person.en import Provider
from time import time
fake1 = Faker()
fake1.seed_instance(0)

addresses = [
    {
        "solar_system": solar_system,
        "planet": planet,
        "country": country,
        "address": address,
    }
    for solar_system in (fake1.safe_color_name() for _ in range(2))
    for planet in (fake1.word() for _ in range(5))
    for country in (fake1.country() for _ in range(10))
    for address in (fake1.address() for _ in range(3))
]

# print(f"addresses: {json.dumps(addresses, indent=2)}")
current_time = int(time())

fake2 = Faker()
data = [{
    "time": current_time,
    "shipment_weight_kg": fake2.pyfloat(left_digits=2,right_digits=2,positive=True,max_value=20),
    "shipment_volume_m3": fake2.pyfloat(left_digits=1,right_digits=3,positive=True,max_value=1),
    "shipment_eta_min": fake2.pyint(min_value=1,max_value=10),
    "shipment_status": "shipped",
    "forecast_origin_wind_velocity_mph": fake2.pyfloat(left_digits=2,right_digits=1,positive=True,max_value=30),
    "forecast_origin_wind_direction": fake2.random_element(["N","W", "S", "E"]),
    "forecast_origin_precipitation_chance": fake2.pyfloat(left_digits=0,right_digits=2,positive=True),
    "forecast_origin_precipitation_kind": fake2.random_element(["rain","snow", "hail", "acid", "fire"]),
    "origin_solar_system": (origin:=fake2.random_element(addresses))["solar_system"],
    "origin_planet": origin["planet"],
    "origin_country": origin["country"],
    "origin_address": origin["address"],
    "destination_solar_system": (destination:=fake2.random_element(addresses))["solar_system"],
    "destination_planet": destination["planet"],
    "destination_country": destination["country"],
    "destination_address": destination["address"],
} for _ in range(10)]

print(f"data: {json.dumps(data, indent=2)}")





# solar_system(2)

# name: varchar


# planet(7/4)

# ->solar_system
# name: varchar


# country

# -> planet
# name: varchar


# address

# ->country
# address: varchar



# forecast

# ->address
# time: int
# ---
# wind_velocity: float
# wind_direction: enum(N,W,S,E)
# precipation_chance: int
# precipation_kind: enum(rain,snow,hail,acid,fire)



# shipment_order

# time: int
# -> origin:address
# -> destination:address
# ---
# weight: float
# volume: float
# eta: int