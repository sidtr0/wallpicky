import struct
import ctypes
import sys
from pathlib import Path

file_name = Path(__file__).stem

PATH = f"C:\\Users\\sidtr\\Documents\\PythonProjects\\wallpicky\\images\\{file_name}.png"

def is_64bit_windows():
    """Check if 64 bit Windows OS"""
    return struct.calcsize('P') * 8 == 64

def changeBG(path):
    """Change background depending on bit size"""
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)

changeBG(PATH)