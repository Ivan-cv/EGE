F = []
for N in range(4,10_000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = R + R[:3]
    else:
        R = '1' + R + '01'
    R = int(R,2)
    if R > 600:
        F.append(R)
print(min(F))




