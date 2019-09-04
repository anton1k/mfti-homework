# Дано трехзначное число. Найдите сумму его цифр.

x = int(input())
s = 0
for _ in range(3):
    y = x % 10
    s += y
    x = x // 10

print(s)