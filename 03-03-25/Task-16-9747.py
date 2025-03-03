from sys import setrecursionlimit

def F(n):
    if n < 11:
        return n
    return n + F(n - 1)

setrecursionlimit(3000)
print(F(2024) - F(2021))