def dell(n,m):
    return n % m == 0

def f(A):
    for x in range(1,10_000):
        f = (dell(x,10) and dell(x,26) and (x >= 300)) <= (A <= x)
        if not f:
            return False
    return True

for A in range(1,10_000):
    if  f(A):
        print(A)