import re
text=input()
print(re.sub("(\w)([A-Z])", r"\1 \2", text))

