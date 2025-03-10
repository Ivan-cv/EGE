def convert(num,sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for N in range(1,1000):
    R = convert(N,12)
    if R % 3 == 0:
        R = str('1' + R + 'B')
    else:
        R = str('2' + R + 'O')
    R = int(R,12)
