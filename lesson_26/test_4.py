'''На шахматной доске заданы координатами 2 различных точек. В первой из них находится конь, во вторую точку ему надо попасть. Выведите координаты клеток, через которые надо прочти коню, чтобы попасть во вторую точку. Путь должен быть кратчайшим, среди имеющихся.

Формат входных данных
Координаты двух клеток, каждая в отдельной строке. Координаты клеток задаются в виде буквы (от a до h) и цифры (от 1 до 8) без пробелов.

Формат выходных данных
Программа должна вывести путь коня, начинающийся и заканчивающийся в данных клетках и содержащий наименьшее число клеток.'''

from collections import deque

x = input()
y = input()


letters = 'abcdefgh'
numbers = '12345678'

graph = dict()
for l in letters:
    for n in numbers:
        graph[l+n] = set()

def add_edge(v1, v2):
    graph[v1].add(v2)
    graph[v2].add(v1)

for i in range(8):
    for j in range(8):
        v1 = letters[i] + numbers[j]
        if 0 <= i + 2 < 8 and 0 < j + 1 < 8:
            v2 = letters[i+2] + numbers[j+1]
            add_edge(v1, v2)

        if 0 <= i - 2 < 8 and 0 < j + 1 < 8:
            v2 = letters[i-2] + numbers[j+1]
            add_edge(v1, v2)

        if 0 <= i + 1 < 8 and 0 < j + 2 < 8:
            v2 = letters[i+1] + numbers[j+2]
            add_edge(v1, v2)

        if 0 <= i - 1 < 8 and 0 < j + 2 < 8:
            v2 = letters[i-1] + numbers[j+2]
            add_edge(v1, v2)

def bfs(graph, x, y):
    distances = {v: None for v in graph}
    parents = {v: None for v in graph}
    distances[x] = 0
    queue = deque([x])
    queue.append(x)
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if distances[v] is None:
                distances[v] = distances[u] + 1
                parents[v] = u
                queue.append(v)
    return parents

parents = bfs(graph, x, y)
path = [y]
parent = parents[y]
while not parent is None:
    path.append(parent)
    parent = parents[parent]

for i in path[::-1]:
    print(i)