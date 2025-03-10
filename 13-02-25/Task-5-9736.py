for n in range(1,10_000):
    r = bin(n)
    if n % 3 == 0:
        n = n + r[:-3]
    else:
        
