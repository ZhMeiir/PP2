import os
Path = input()
if os.path.exists(Path):
    os.remove(Path)
    print("removed")
else:
    print("Path doesnt exists")