def f(B):
    for x in range (1,10_000):
        for y in range (1,10_000):

            f = ((x&500!=0) and (x&200 == 0)) <= (not (x&B==0))
            if f:
                return False
    return True


