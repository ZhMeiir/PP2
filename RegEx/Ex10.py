import re

text = input()

print(re.sub("(?<=[a-z])(?=[A-Z])", "_", text).lower())
