'''Заданная цифра в числе
Сколько раз цифра d входит в десятичную запись числа n?

Входные данные

Число 0≤d≤9. Пробел. Целое положительное число n в десятичной системе (0 ≤ n ≤ 3·10 6) .

Выходные данные

Сколько раз цифра d входит в запись числа n.'''

s = input().split()
res = 0

for i in s[1]:
    if i == s[0]:
        res += 1

print(res)