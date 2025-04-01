from planets import read_planets
from materials import read_materials
from rockets import read_rockets
import sys
import csv
import os


def main():
    print()
    print("---SPACEMETRICS---")
    print()
    main_menu()


def main_menu():
    """ 
    Displays shield main menu and handles user selection.
    """
    while True:
        print()
        print("---MAIN MENU---")
        print()
        print("1 - Solar System")
        print("2 - Space Rockets")
        print("3 - Materials")
        print("4 - Help")
        print()
        print("5 - Exit")
        print()

        choice = int(input("Enter: "))

        if choice == 1:
            solar_system()
        elif choice == 2:
            rockets()
        elif choice == 3:
            materials()
        elif choice == 4:
            help_menu()
        elif choice == 5:
            sys.exit()
        else:
            print("Invalid input, please try again.")


def help_menu():
    """ 
    Displays help information.
    """
    while True:
        print()
        print("------HELP------")
        print()
        print("1 - Explore solar system with precise description of each planet.")
        print("2 - Check which rockets are available and what are ther capabilities.")
        print("3 - Analyze materials used in outer space.")
        print()
        print("1 - Back")
        print()

        try:
            back = int(input("Enter: "))
        except ValueError:
            print("Invalid input, please try again.")

        if back == 1:
             main_menu()
        else:
            print("Invalid input, please try again.")


def solar_system():
    """
    Displays available planets.
    Contains detailed information about each planet.
    """
    # read planets form csv file
    planets = read_planets()
    # create dictionary with names and mapping
    planet_mapping = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
        9: "Pluto"
    }

    while True:
        print()
        print("---SOLAR SYSTEM---")
        print()
        print("1 - Mercury")
        print("2 - Venus")
        print("3 - Earth")
        print("4 - Mars")
        print("5 - Jupiter")
        print("6 - Saturn")
        print("7 - Uranus")
        print("8 - Neptune")
        print("9 - Pluto")
        print()
        print("0 - Back")

        try:
            choice = int(input("Enter: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        if choice == 0:
            main_menu()
        # get planet name from mapping
        planet_name = planet_mapping.get(choice, None)
        # check if planet name is nor None
        if planet_name:
            # get planet from list of planets
            planet = next((p for p in planets if p.name.strip().lower() == planet_name.lower()), None)
            if planet:
                print(planet)
            else:
                print("Planet not found.")
        else:
            print("Invalid input. Please try again.")


def rockets():
    """
    Displays companies producing space rockets.
    Contains detailed information about payloads.
    """
    # read materials form csv file
    rockets = read_rockets()

    if not rockets:
        print("No rockets data available.")
        return

    # create dictionary with names and mapping
    rocket_mapping = {
        1: "Arianspace",
        2: "Blue Origin",
        3: "Relativity Space",
        4: "SpaceX",
        5: "ULA",
    }

    while True:
        print()
        print("---SPACE COMPANIES---")
        print()
        print("1 - Arianspace")
        print("2 - Blue Origin")
        print("3 - Relativity Space")
        print("4 - SpaceX")
        print("5 - ULA")
        print()
        print("0 - Back")
    
        try:
            choice = int(input("Enter: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        if choice == 0:
            return
        # get rocket name from mapping
        company_name = rocket_mapping.get(choice, None)
        # check if rocket name is not None
        if company_name:
            print(f"Rockets from: {company_name}")

            company_rockets = [r for r in rockets if r.company.lower() == company_name.lower()]

            if company_rockets:
                print(f"---{company_name}---")
                for rocket in company_rockets:
                    print(rocket)
            else:
                print("No rockets found.")
        else:
            print("Invalid input. Please try again.")


def materials():
    """
    Displays available materials used in space engineering.
    Contains detailed information about certain material.
    """
    # read materials form csv file
    materials = read_materials()
    # create dictionary with names and mapping
    material_mapping = {
        1: "Aluminum",
        2: "Titanium",
        3: "Carbon Fiber",
        4: "Aerogel",
        5: "Polymer",
        6: "Kevlar",
        7: "Regolith",
        8: "Water",
    }

    while True:
        print()
        print("---SPACE MATERIALS---")
        print()
        print("1 - Aluminum")
        print("2 - Titanium")
        print("3 - Carbon Fiber")
        print("4 - Aerogel")
        print("5 - Polymer")
        print("6 - Kevlar")
        print("7 - Regolith")
        print("8 - Water")
        print()
        print("0 - Back")

        try:
            choice = int(input("Enter: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        if choice == 0:
            main_menu()
        # get material name from mapping
        material_name = material_mapping.get(choice, None)
        # check if material name is not None
        if material_name:
            # get material form list of materials
            material = next((m for m in materials if m.name.strip().lower() == material_name.lower()), None)
            if material:
                print(material)
            else:
                print("Material not found.")
        else:
            print("Invalid input. Please try again.")


def shield_constructor():
    ...


def unit_converter():
    ...


if __name__ == "__main__":
    main()