def all_true(tup):
    return all(tup)
tup=list()
while True:
    value = input()
    if not value:
        break
    tup += (eval(value))
if all_true(tup):
    print("All elements in the tuple are true")
else:
    print("All elements are not true")