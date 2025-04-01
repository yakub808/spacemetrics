import csv
import os
from data_path import resource_path


class Material:
    def __init__(self, name, type, density, strength, radiation_shielding, emissivity, thermal_conductivity, heat_capacity, exterior_applications, interior_applications, destination):
        self.name = name
        self.type = type
        self.density = float(density)
        self.strength = float(strength)
        self.radiation_shielding = radiation_shielding
        self.emissivity = float(emissivity)
        self.thermal_conductivity = float(thermal_conductivity)
        self.heat_capacity = float(heat_capacity)
        self.exterior_applications = exterior_applications
        self.interior_applications = interior_applications
        self.destination = destination


    def __repr__(self):
        return f"{self.name} \n| {self.type} \n| radiation shielding: {self.radiation_shielding} \n| emissivity: {self.emissivity} \n| thermal_conductivity: {self.thermal_conductivity}W/mK \n| heat capacity: {self.heat_capacity}J/kg*K \n| exterior use: {self.exterior_applications} \n| interior use: {self.interior_applications}"


def read_materials():
    materials = []

    try:
        with open(resource_path('data/materials.csv'), 'r') as file:
            material_reader = csv.DictReader(file)

            for row in material_reader:
                row = {key.strip(): value.strip() for key, value in row.items()}
                
                if all(key in row for key in ['name', 'type', 'density', 'strength', 'radiation_shielding', 'emissivity', 'thermal_conductivity', 'heat_capacity', 'exterior_applications', 'interior_applications', 'destination']):
                    material = Material(
                        row['name'],
                        row['type'],
                        row['density'],
                        row['strength'],
                        row['radiation_shielding'],
                        row['emissivity'],
                        row['thermal_conductivity'],
                        row['heat_capacity'],
                        row['exterior_applications'],
                        row['interior_applications'],
                        row['destination']
                    )
                    materials.append(material)

    except FileNotFoundError:
        print("File not found.")

    return materials