'''На вход программе подается последовательность чисел, заканчивающихся нулем. Сам ноль не входит в последовательность. Найти среднее значение последовательности. Для округления использовать функцию round(x, n). Где x - число, n - количество знаков после запятой.

Формат входных данных
Последовательность чисел, заканчивающихся нулем. Одно число в строку.

Формат выходных данных
Одно число — среднее значение. Округлить до двух цифр после запятой.'''
n = 0
s = 0
while True:
    x = int(input())
    if x == 0:
        break
    s += x
    n += 1
print(round(s/n, 2))
