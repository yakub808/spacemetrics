import os
import sys


def resource_path(relative_path):
    """
    Returns the absolute path to the data file.
    """
    try:
        # when script is frozen with pyinstaller, use sys.MEIPASS for base path
        base_path = sys.MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)