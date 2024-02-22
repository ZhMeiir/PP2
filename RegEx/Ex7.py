import re

a = input()
x = re.split("_", a)
for i in range(1, len(x)):
    x[i] = x[i][0].upper() + x[i][1:]
result = ''.join(x)
print(result)