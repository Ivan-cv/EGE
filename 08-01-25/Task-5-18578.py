def convert (num,sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
for N in range(1, 10_000):
    R = convert(N,4)
    if R % 4 == 0:
        str('2' + R + '03')
    else:
        


