from itertools import permutations, product

def f(x,y,z,w):
    return (w <= (not (z <= w))) or y

for a1, a2, a3, a4, a5, a6, a7 in product([0,1], repeat=7):
    table = [(1,a1, a2, a3), (0,1,0,a4), (a5,0,a6,a7)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            u = (f(**dict(zip(p,t)))for t in table)
            if u:
                print(*p)