def f(A):
    for x in range (1, 10_000):
        for y in range(1, 10_000):
            f = (y > 10) or (x * A > y + x )
            if not f:
                return False
    return True

for A in range (1, 10_000):
    if f(A):
        print(A)
        break
