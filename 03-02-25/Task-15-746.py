from itertools import combinations

def f(x):
    P = 12 <= x  <= 26
    Q = 30 <= x <= 53
    A = A1 <= x <= A2
    return (A <= P) or Q

ans = []
line = [i /10 for i in range(0 * 10, 70)]

for A1, A2 in combinations(line,2):
     if all(f(x) for x in line):
         ans.append(A2 - A1)

print(max(ans))
