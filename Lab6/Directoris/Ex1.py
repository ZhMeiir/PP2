import os

path = input()
os.chdir(path)
print(os.listdir())
