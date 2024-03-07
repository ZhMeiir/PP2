file1 = open(r"C:\Users\meiir\OneDrive\Рабочий стол\Meiir.txt", "r")
file2 = open(r"C:\Users\meiir\OneDrive\Рабочий стол\Meiir2.txt", "w")
info = file1.read()
file2.write(info)
file1.close()
file2.close()


file2 = open(r"C:\Users\meiir\OneDrive\Рабочий стол\Meiir2.txt", "r")
print(file2.read())
file2.close()