print('x,y,z,w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not w) and ((y or z) <= (y and (not x)))
                if not f:
                    print(x,y,z,w)


