'''Числа трибоначчи - последовательность целых чисел {t n }, заданная с помощью рекуррентного соотношения: t 0 = 0, t 1 = 0, t 2 = 1 , t n+3 = t n + t n+1 + t n+2 Нужно найти номер первого числа трибоначчи, превосходящего заданное. Нумерация начинается с 0 .

Формат входных данных
Одно целое число.

Формат выходных данных
Одно число — номер первого числа трибоначчи, превосходящее заданное во входных данных число.'''

n = int(input())
i = 0
a = [0,0,1]
while i <= n+3:
    a.append(sum(a[-3:]))
    if a[i] > n:
        print(i)
        break
    i += 1