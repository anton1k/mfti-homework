'''Дан невзвешенный связный граф. Вершины пронумерованы от 0. Трeбуется с помощью обхода в ширину найти расстояние от одной указанной вершины до другой.
Формат входных данных
На вход программе в первой строке подаются через пробел четыре числа: n, m, x, y. 
Число n (2 <= n <= 1000) - количество вершин в графе, m (1 <= m <= 20000) - количество ребер. x и y - начальная и конечная вершины соответственно (0 <= x,y < n). В следующих m строках задаются ребра, по два числа в каждой строке - номера соединенных вершин.
Формат выходных данных
Требутеся распечатать одно число - расстояние от вершины x до вершины y .'''


# n, m, x, y = 8, 10, 5, 2
# graph = {0: {1, 2, 4}, 1: {0, 3, 5}, 2: {0, 5}, 3: {1, 4, 5}, 4: {0, 3, 6, 7}, 5: {1, 2, 3}, 6: {4}, 7: {4}}
from collections import deque

n, m, x, y = map(int, input().split())
graph = {i:set() for i in range(n)}

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)

def bfs(graph, x, y):
    distances = [None]*n
    distances[x] = 0
    queue = deque([x])
    queue.append(x)
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if distances[v] is None:
                distances[v] = distances[u] + 1
                queue.append(v)
    return distances[y]

print(bfs(graph, x, y))

