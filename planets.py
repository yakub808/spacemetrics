import csv
import os
from data_path import resource_path


class Planet:
    def __init__(self, name, type, distance, temp_day, temp_night, gravity, atmosphere, solar_radiation, water, soil, minerals, planetary_heat):
        self.name = name
        self.type = type
        self.distance = float(distance)
        self.temp_day = float(temp_day)
        self.temp_night = float(temp_night)
        self.gravity = float(gravity)
        self.atmosphere = atmosphere
        self.solar_radiation = float(solar_radiation)
        self.water = water
        self.soil = soil
        self.minerals = minerals
        self.planetary_heat = float(planetary_heat)

    def __repr__(self):
        return f"{self.name} | {self.type} | atmosphere: {self.atmosphere} | temp-day: {self.temp_day}C | temp-night: {self.temp_night}C | gravity: {self.gravity}g | radiation: {self.solar_radiation}W/m2 | heat: {self.planetary_heat}W"



def read_planets():
    planets = []

    try:
        # Open the CSV file for reading
        with open(resource_path('data/solar_system.csv'), 'r') as file:
            planet_reader = csv.DictReader(file)

            for row in planet_reader:
                # Clean up the row by stripping spaces and lowercasing keys
                row = {key.strip().lower(): value.strip() for key, value in row.items()}

                # Ensure all required fields exist and load the planet
                if all(key in row for key in ['name', 'type', 'distance', 'temp_day', 'temp_night', 'gravity', 'atmosphere', 'solar_radiation', 'water', 'soil', 'minerals', 'planetary_heat']):
                    planet = Planet(
                        row['name'],
                        row['type'],
                        row['distance'],
                        row['temp_day'],
                        row['temp_night'],
                        row['gravity'],
                        row['atmosphere'],
                        row['solar_radiation'],
                        row['water'],
                        row['soil'],
                        row['minerals'],
                        row['planetary_heat']
                    )
                    planets.append(planet)
    except FileNotFoundError:
        print("File not found.")

    return planets