let = ord('A')
for i in range(1, 27):
    file = open(f"dirFile\\task6_alphabet\\{chr(let)}.txt", "x")
    let += 1
    file.close()
