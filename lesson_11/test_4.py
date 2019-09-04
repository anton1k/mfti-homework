'''Модифицируйте алгоритм вычисления значений целевой функции так, чтобы вычислить значения prev[i], и восстановите траекторию наименьшей стоимости из точки 1 в точку n.'''

def calculate_min_cost(n, price):
    C = [float('-inf'), price[1], price[1]+price[2]] + [0]*(n-2)
    path = []
    for i in range(3, n+1):
        C[i] = price[i] + min(C[i-1], C[i-2])
        if C[i-1] < C[i-2]:
            path.append(i-1)
        else:
            path.append(i-2)

    return path

