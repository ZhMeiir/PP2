import string
a=input()
s=sum(1 for i in a if i<='Z' and i>='A')
d=sum(1 for i in a if i<='z' and i>='a')


print("Uppercase letters:",s) 
print("Lowercase letters:", d)