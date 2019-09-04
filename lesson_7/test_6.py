'''Необходимо найти НОД двух чисел, используя алгоритм Евклида.

Формат входных данных
На вход подаются два натуральных числа, по числу в новой строке.

Формат выходных данных
Одно число - НОД входных чисел.'''

a = int(input())
b = int(input())

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
 
print(a + b)