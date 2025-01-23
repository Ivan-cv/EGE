def convert(num,sys):
    res = ''
    while num:
        res +=(num % sys)
        num //= sys
    return res[::-1]
for n in range(1, 10_000):
    r = convert(n,3)
    if sum(map(int,r)) % 3 == 0:
        r = '20' + r
    else:
        r = '10' + r
