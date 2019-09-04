'''Вам даны 2 координаты 2 клеток на шахматном поле. Нужно ответить на вопрос, можно ли попасть из одной клетки в другую за не более чем 2 хода конем. В случае, если попасть возможно, надо вывести количество ходов, за которое это можно сделать. Если попасть невозможно, следует вернуть -1.

Формат входных данных
На вход подаются числа от 1 до 8 в 4 строках. Первые 2 строки задают координаты начальной клетки, вторые 2 -- координаты конечной клетки.

Формат выходных данных
Одно число — количество ходов, за которые можно попасть из из одной клетки во вторую. Если невозможно -- вывести -1.'''
# x1, y1, x2, y2 = 1, 1, 8, 8

x1, y1, x2, y2 = int(input())-1, int(input())-1, int(input())-1, int(input())-1

board = [[0]*8 for i in range(8)]

board[x1][y1], board[x2][y2] = -1, -2

def horse(x1, y1, x2, y2):

    if x1 == x2 and y1 == y2:
        return 0

    for x,y in [[2,1], [2,-1], [1,-2], [-1,-2], [-2,-1], [-2,1], [-1,2], [1,2]]:
        if x1+x >= 0 and x1+x < 8 and y1+y >= 0 and y1+y < 8:
            if board[x1+x][y1+y] == -2:
                return 1
            board[x1+x][y1+y] = board[x1][y1] if board[x1][y1] > 0 else 0 + 1
                
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                for x,y in [[2,1], [2,-1], [1,-2], [-1,-2], [-2,-1], [-2,1], [-1,2], [1,2]]:
                    if i+x >= 0 and i+x < 8 and j+y >= 0 and j+y <= 8:
                        if board[i+x][j+y] == -2:
                            return 2

    return -1
            
print(horse(x1, y1, x2, y2))