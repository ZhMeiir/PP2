def fucn(n):
    for i in range(0, n+1, 2):
        yield(i)
n=int(input())
print(", ".join(str(i) for i in fucn(n)))