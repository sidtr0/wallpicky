# wallpicky

A wallpaper changing script (tested for Windows 10 only).

## How to use wallpicky?

1. Put the image you want to set as your wallpaper in the `images/` folder.
2. Make a new Python file with the same name as the image you put in the `images/` folder, in the `scripts/` folder with the same content as the other scripts in the folder.
   (TODO: Create a script to create a new script!)
3. Schedule the script to be run on the Task Scheduler app on Windows 10.

### Example usage

Let's say you have an image called `afternoon.png` (can be any valid image format used by Windows 10 for wallpapers). Put this image in the `images/` folder and make a new script caled `scripts/afternoon.py` with the following content:

```py
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
```

Schedule this script in Task Scheduler and it should work like a breeze.
