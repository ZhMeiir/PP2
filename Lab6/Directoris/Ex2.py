import os

def check_path(Path):
    if os.path.exists(Path):
        print("exists")
    else:
        print("Doesnt exist")
    if os.access(Path, os.R_OK):
        print("readable")
    else:
        print("not readable")
    if os.access(Path, os.W_OK):
        print("writable")
    else:
        print("unwritable")
    if os.access(Path, os.X_OK):
        print("executable")
    else:
        print("not executable")

Path = input()
check_path(Path)
