"""
    Setup for the MainEdge application.

    Employee Database Manager (for Human Resources)
    Copyright (c) New York Power Authority 2018. All Rights Reserved.
    Digital Analytics Team - David Morfe <david.morfe@nypa.gov>.
"""

import cx_Freeze
import sys
import matplotlib
import numpy
import pandas
import os
base = None

if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("MainEdge.py", base = base, icon = "C:\\Users\\DaviMabi\\Desktop\\MainEdge\\nypaLOGO.ico")]

os.environ['TCL_LIBRARY'] = r'C:\\Program Files\\Python36\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\\Program Files\\Python36\\tcl\\tk8.6'

cx_Freeze.setup(
    name = "MainEdge-Installer",
    options = {"build_exe": {"packages": ["tkinter", "matplotlib", "pandas", "numpy", "time"],
                             "include_files": [os.path.join('C:\\Program Files\\Python36', 'DLLs', 'tk86t.dll'),
                                               os.path.join('C:\\Program Files\\Python36','DLLs', 'tcl86t.dll'),
                                               "nypa2.png", "nypa4.png"]}},
    version = "0.1",
    description = "A Human Resources Employee Database Manager",
    executables = executables
    )
