import re
a=input()
print(re.sub("[\s , .]+", ":" , a))