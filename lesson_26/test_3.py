'''Дано прямоугольное поле размера n строк на m столбцов. Некоторые ячейки поля непроходимы. Требуется найти расстояние между двумя заданными ячейками.

Формат входных данных
В первой строке два числа — n и m (1 <= n,m <= 500) . Во второй — номер строки и столбца начальной ячейки, в третьей — номер строки и столбца конечной ячейки. В остальных n строках задано поле. Каждая строка поля содержит m символов, X задает непроходимую ячейку, «пробел» — проходимую.

Формат выходных данных
Вывести одно число — расстояние между указанными ячейками (ходить можно только по горизонтали или вертикали). Если пути между этими ячейками нет, выведите "INF" без кавычек.'''

# n, m, = 5, 7
# start = [3, 5]
# end = [1, 1]
# field = [
#     ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
#     ['X', ' ', 'X', ' ', ' ', ' ', 'X'],
#     ['X', ' ', 'X', ' ', 'X', ' ', 'X'],
#     ['X', ' ', ' ', ' ', 'x', ' ', 'x'],
#     ['X', 'X', 'X', 'X', 'X', 'X', 'X']
#     ] # 10
# field = [
#     ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
#     ['X', ' ', 'X', ' ', ' ', ' ', 'X'],
#     ['X', ' ', 'X', 'X', 'X', ' ', 'X'],
#     ['X', ' ', ' ', ' ', 'X', ' ', 'X'],
#     ['X', 'X', 'X', 'X', 'X', 'X', 'X']
# ] # INF

from collections import deque

n, m, = map(int, input().split())
start = [int(i) for i in input().split()]
end = [int(i) for i in input().split()]
field = [list(input()) for i in range(n)]
graph = dict()

for i in range(n):
    for j in range(m):
        graph[str(i) + str(j)] = set()
        if (i + 1 < n and i - 1 >=0) and (j + 1 < m and j - 1 >=0):
            if field[i][j] == ' ':
                if field[i+1][j] == ' ':
                    graph[str(i) + str(j)].add(str(i+1) + str(j))
                if field[i-1][j] == ' ':
                    graph[str(i) + str(j)].add(str(i-1) + str(j))
                if field[i][j-1] == ' ':
                    graph[str(i) + str(j)].add(str(i) + str(j-1))
                if field[i][j+1] == ' ':
                    graph[str(i) + str(j)].add(str(i) + str(j+1))
                

def bfs(graph, x, y):
    distances = {v: None for v in graph}
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

x = str(start[0]) + str(start[1])
y = str(end[0]) + str(end[1])
res = bfs(graph, x, y)

print(res if res else 'INF')






