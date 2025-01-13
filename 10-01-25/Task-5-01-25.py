def convert(num,sys):
    res = ''
    while num:
        res+= str(num % sys)
        num //= sys
    return res[::-1]
for N in range(1,10):
    R = convert(N,3)
    if