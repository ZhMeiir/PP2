import math
lebg=int(input())
sides=int(input())

area=sides*lebg*(lebg/(2*math.tan(math.pi/sides)))/2

print("area=", area)
