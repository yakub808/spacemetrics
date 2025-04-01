from rockets import read_rockets, Rocket
from project import materials, rockets, solar_system

def test_read_rockets():
    """
    Tests the read_rockets function from the project module.
    """
    rockets_list= read_rockets()
    assert len(rockets_list) > 0, "Rocket list should not be empty."
    assert isinstance(rockets_list[0], Rocket), "First element should be an object."


def test_materials():
    """
    Test if materials() function exists and can be called.
    """
    assert callable(materials), "materials() function should be callable."

def test_rockets():
    """
    Test if materials() function exists and can be called.
    """
    assert callable(rockets), "rockets() function should be callable."

def test_solar_system():
    """
    Test if materials() function exists and can be called.
    """
    assert callable(solar_system), "solar_system() function should be callable."