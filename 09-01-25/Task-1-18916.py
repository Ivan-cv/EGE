from itertools import permutations

graph = 'АВ АБ ВГ ГЕ ЕЗ ЗЖ ЖД ДБ ЕЖ'.split()
matrix = '356 358 128 67 127 147 456 23'.split()

print(*range(1,9))
for i in permutations('А Б В Г Е З Ж Д'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)]for x, y in graph):
        print(*i)