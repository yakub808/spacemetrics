import csv
import os
from data_path import resource_path

# define rocket class
class Rocket:
    def __init__(self, company, rocket, crew_capacity, payload_max, payload_diameter, payload_height, payload_volume, fuel_type, destination, status):
        self.company = company
        self.rocket = rocket
        self.crew_capacity = int(crew_capacity)
        self.payload_max = float(payload_max)
        self.payload_diameter = float(payload_diameter)
        self.payload_height = float(payload_height)
        self.payload_volume = float(payload_volume)
        self.fuel_type = fuel_type
        self.destination = destination
        self.status = status

    # clarifies output and helps in debugging
    def __repr__(self):
        return f"{self.company} | {self.rocket} | status: {self.status} | crew: {self.crew_capacity} | payload: {self.payload_max}kg | payload volume: {self.payload_volume}m3 mission: {self.destination}"
    
# read rocket from csv
def read_rockets():
    # create epmty list to store rockets
    rockets = []

    try:
        # open certain csv file
        with open(resource_path('data/rockets.csv'), 'r') as file:
            rocket_reader = csv.DictReader(file)

            for row in rocket_reader:
                # Clean up the row by stripping spaces and lowercasing keys
                row = {key.strip(): value.strip() for key, value in row.items()}

                if all(key in row for key in ['company', 'rocket', 'crew_capacity', 'payload_max', 'payload_diameter', 'payload_height', 'payload_volume', 'fuel_type', 'destination', 'status']):
                    rocket = Rocket(
                        row['company'],
                        row['rocket'],
                        row['crew_capacity'],
                        row['payload_max'],
                        row['payload_diameter'],
                        row['payload_height'],
                        row['payload_volume'],
                        row['fuel_type'],
                        row['destination'],
                        row['status']
                    )
                    rockets.append(rocket)

    except FileNotFoundError:        
        print("File not found.")

    return rockets
        