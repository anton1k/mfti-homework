'''Реализовать алгоритм поиска выигрышных и проигрышных позиций в аналогичной игре, но ходы делает король (только вправо, вниз и по диагонали).'''

def king(n, m):
    P = [['0']*m for i in range(n)]
    P[n-1][m-1] = '-' # нижняя правая клека всегда проигрышная
    
    for i in range(n-1, -1,-1):
        for j in range(m-1, -1,-1):

            if P[i][j] == '-': # если клетка определана как проигрышная расставляем + там от куда можно получить доступ к этой клетке
                if P[i-1][j] == '0':
                    P[i-1][j] = '+'
                if P[i][j-1] == '0':
                    P[i][j-1] = '+'
                if P[i-1][j-1] == '0':
                    P[i-1][j-1] = '+'

            if P[i][j] == '+': # если клетка определана как выиграшная расставляем - там от куда можно получить доступ к этой клетке
                if P[i-1][j] == '0':
                    P[i-1][j] = '-'
                if P[i][j-1] == '0':
                    P[i][j-1] = '-'
                if P[i-1][j-1] == '0':
                    P[i-1][j-1] = '-'

    return P

for i in king(6, 8):
    print(i)