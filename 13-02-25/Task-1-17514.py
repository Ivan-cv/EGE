from itertools import permutations

graph = 'AB AH BH FG FD GC DC CE EA'.split()
matrix = '53 1 2 13 30 8 74 5 3 21'.split()

print(*(range(1,9)))

for i in permutations ('A B C D E F G H'):
    for x, y in graph:
        if all(str(i.index(x) + 1)in matrix[i.index(y)] for x,y in graph):
            print(*i)