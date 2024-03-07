file = open(r"C:\Users\meiir\OneDrive\Рабочий стол\Meiir.txt", "r")
count = 0
for line in file:
    count += 1
print("Number of lines:", count)
file.close()