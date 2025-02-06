from itertools import combinations

def f(x):
    B = 18 <= x <= 52
    C = 16 <= x <= 41
    A = A1 <= x <= A2
    return((B <= A) or (not(C and A)))

ans = []
line = [i/10 for i in range(160, 520)]
for A1,A2 in combinations(line,2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(max(ans))