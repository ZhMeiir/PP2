def func(n):
    for i in range(n+1):
        yield(i**2)
n=int(input())
for i in func(n):
    print(i)
