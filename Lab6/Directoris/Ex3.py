import os

Path = input()
if os.path.exists(Path):
    print(os.path.basename(Path))
    print(os.path.dirname(Path))
else:
    print("doesnt exits")