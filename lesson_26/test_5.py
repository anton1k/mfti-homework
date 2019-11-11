'''Дан невзвешенный неориентированный связный граф. Вершины пронумерованы от 0. Трeбуется с помощью обхода в ширину построить остовное дерево.

Формат входных данных
На вход программе в первой строке подаются через пробел два числа: n (2 <= n <= 1000) — число вершин в графе и m (1 <= m <= 20000) — число рёбер. В следующих m строках задаются ребра: по два числа в каждой строке — номера соединённых вершин.

Формат выходных данных
Требуется распечатать n-1 пару чисел, каждyю на новой строке. Каждая пара задаёт ребро в остовном дереве.'''
# n, m = 6, 7
# graph = {0: {1, 2}, 1: {0, 2, 4, 5}, 2: {0, 1, 3, 5}, 3: {2}, 4: {1}, 5: {1, 2}}

from collections import deque
n, m, = map(int, input().split())
graph = {i:set() for i in range(n)}

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)

def bfs(graph):
    distances = [None]*n
    x = 0
    res = []
    distances[x] = 0
    queue = deque([x])
    queue.append(x)
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if distances[v] is None:
                distances[v] = distances[u] + 1
                res.append([v, u]) #добавляем ребра
                queue.append(v)
    return res

for i in bfs(graph):
    print(' '.join(str(x) for x in i))

