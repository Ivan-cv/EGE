from itertools import permutations

graph = 'AF AB BF FG GE EH HD DC EC CA'.split()
matrix = '68 47 45 237 368 15 248 157'.split()

print(*range(1, 8))
for i in permutations('ABFGEHDC'):
        if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
            print(*i)