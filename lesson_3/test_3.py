# Требуется определить, является ли данный год високосным. (Год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400).
x = int(input())

if (x%4 == 0 and x%100 != 0) or x%400 == 0:
    print('YES')
else:
    print('NO')