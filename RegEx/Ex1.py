import re

a=input()
data=open('row.txt')
data.read(print(re.findall("a.b*", a)))