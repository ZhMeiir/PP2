import re

a = input()
print(re.split("(?<=[a-z])(?=[A-Z])", a ))
