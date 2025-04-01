## SPACEMETRICS
### Video Demo: [SPACEMETRICS VIDEO](https://youtu.be/go0W7LgOKU0)
### Description:
SPACEMETRICS is an application written in Python language. Application provides detailed info about:
planets in our Solar System, available space rocket systems and specification of materials used in outer space environment.
The application is aimed for space engineers and mission planners, program relies on external CSV files for databases.
Application can be used for educational and informational purposes.

**DATA STORAGE**

SPACEMETRICS reads data from external CSV files and processes it using dedicated classes. 
Each dataset is structured as follows:

Planets:
- name of a planet: stored as a string;
- type of a planet: stored as a string;
- distance form Earth: stored as float in AU;
- day temperature on a planet: stored as float in C;
- night temperature on a planet: stored as float in C;
- gravity force: stored as float in g;
- composition of an atmosphere: stored as a string;
- solar radiation: stored as float in W/m2;
- presence of water: stored as a string;
- composition of surface: stored as a string;
- planetary heat: stored as a float in W.

The information about planets is stored in 'Planet' class in 'planets.py'. Each planet is assigned a name and ID number. 
The ID number corresponds to the planet's location within the solar system.

Rockets:
- name of a company: stored as a string;
- name of a rocket: stored as a string;
- crew capacity: stored as int;
- max payload weight: stored as float in kg;
- payload diameter: stored as float in m;
- payload height: stored as float in m;
- payload volume: stored as float in m3;
- rocket destination: stored as a string;
- rocket availability: stored as a string;

The information about rockets is stored in 'Rocket' class in 'rockets.py'. Each rocket is assigned to a company. 

Materials:
- name of a material: stored as a string;
- type of a material: stored as a string;
- density of a material: stored as a float in kg/m3;
- strength: stored as float in MPa
- radiation shielding: stored as a string;
- emissivity: stored as float in e
- thermal conductivity: stored as float in W/mK
- heat capacity: stored as float in J/kg*K
- exterior applications: stored as a string;
- interior application: stored as a string;
- destination: stored as a string;

The information about materials is stored in 'Material' class in 'materials.py'. Each material is assigned a name and ID number.

**THE main() FUNCTION**
The main() function initializes the program, prints title for SPACEMETRICS application and calls to main_menu() function.

**THE main_menu() FUNCTION**
The main_menu() function prints out the main menu of the SPACEMETRICS application.

**THE help_menu() FUNCTION**
The help_menu() function provides a clear guide for using the SPACEMETRICS application. It outlines the available menu options, making the program easy to navigate even for first-time users.

**THE solar_system() FUNCTION**
The solar_system() function enables users to search for a planet from the SPACEMETRICS database by ID number. Function processed user input, checks for validation of the data and displays detailed information about the selected planet in organized format. If the planet is not found, function informs the user with an error message.
Function reaches out to 'planets.py' and 'solar_system.csv' files.

**THE rockets() FUNCTION**
The rockets() function enables users to search for a rocket from the SPACEMETRICS database by company name. Function processed user input, checks for validation of the data and displays detailed information about the rockets from certain company in organized format. If rocket is not found, function informs the user with an error message.
Function reaches out to 'rockets.py' and 'rockets.csv' files.

**THE materials() FUNCTION**
The materials() function enables users to search for a material from the SPACEMETRICS database by ID number. Function processed user input, checks for validation of the data and displays detailed information about the material in organized format. If material is not found, function informs the user with an error message.
Function reaches out to 'materials.py' and 'materials.csv' files.

**THE read_planets() FUNCTION**
The read_planets() function is used to create a list of available planets and acquires information about each of them from connected csv file.

**THE read_rockets() FUNCTION**
The read_rockets() function is used to create a list of available rockets and acquires information about each of them from connected csv file.

**THE read_materials() FUNCTION**
The read_materials() function is used to create a list of materials used in outer space and acquires information about each of them from connected csv file.

**FUTURE ENHANCEMENTS**
1. Add unit converter.
2. Add shield constructor.
3. Add thermal transfer calculator.
4. Add 3D models.
5. Upgrade interface.
