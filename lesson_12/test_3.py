# На шахматной доске стоят белый король и черный конь. Конь неподвижен, король может ходить на одну клетку вправо, на одну клетку вверх или наискосок вправо-вверх. Посчитайте, сколькими способами король может дойти до клетки h8, начав с клетки a1. Королю нельзя попадать под атаку коня. Самого коня есть тоже нельзя.

# Строки шахматной доски пронумерованы числами от 1 до 8, столбцы буквами от a до h. Строка 1 - самая нижняя, столбец a - самый левый.

# Формат входных данных
# В единственной строке - позиция коня. Позиция - это два символа, буква столбца и номер строки, например a3.

# Формат выходных данных
# Одно число — результат.

poz = input()

def king(poz):
    board = [[0]*8 for i in range(8)]
    y1 = -1
    x1 = int(poz[1])-1
    s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    for i in s:
        if poz[0] == i:
            y1 = s.index(i)

    board[x1][y1] = -1
    board[0][0] = 1

    for x,y in [[2,1], [2,-1], [1,-2], [-1,-2], [-2,-1], [-2,1], [-1,2], [1,2]]:
            if x1+x >= 0 and x1+x < 8 and y1+y >= 0 and y1+y < 8:
                board[x1+x][y1+y] = board[x1][y1]

    if board[7][7] == -1:
        return 0

    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                if i-1 >= 0:
                    board[i][j] += board[i-1][j] if board[i-1][j] > 0 else 0 
                if j-1 >= 0:
                    board[i][j] += board[i][j-1]  if board[i][j-1] > 0 else 0 
                if i-1 >= 0 and j-1 >= 0:
                    board[i][j] += board[i-1][j-1] if board[i-1][j-1] > 0 else 0 

    return board[7][7]           

print(king(poz))