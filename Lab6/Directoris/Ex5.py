file = open(r"C:\Users\meiir\OneDrive\Рабочий стол\Meiir.txt", "w")
file.write(str([i for i in input().split()]))
file.close()

file = open(r"C:\Users\meiir\OneDrive\Рабочий стол\Meiir.txt", "r")
print(file.read())