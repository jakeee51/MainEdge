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

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "MainEdge",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]\\MainEdge.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     "TARGETDIR"               # WkDir
     )
    ]
msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {"data": msi_data}

executables = [cx_Freeze.Executable("MainEdge.py", base = base, icon = "C:\\Users\\DaviMabi\\Desktop\\MainEdge App\\nypaLOGO.ico")]

os.environ['TCL_LIBRARY'] = r'C:\\Program Files\\Python36\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\\Program Files\\Python36\\tcl\\tk8.6'

cx_Freeze.setup(
    name = "MainEdge",
    options = {"build_exe": {"packages": ["tkinter", "matplotlib", "pandas", "numpy", "time"],
                             "include_files": [os.path.join('C:\\Program Files\\Python36', 'DLLs', 'tk86t.dll'),
                                               os.path.join('C:\\Program Files\\Python36','DLLs', 'tcl86t.dll'),
                                               "nypa2.png", "nypa4.png"]},
               "bdist_msi": bdist_msi_options,},
    version = "0.1",
    author = "David J. Morfe"
    description = "A Human Resources Employee Database Manager",
    executables = executables
    )
