# По данному натуральному числу N распечатайте все квадраты натуральных чисел, не превосходящие N , в порядке возрастания.

# ВАЖНО! В данной задаче необходимо использовать цикл.

n = int(input())
i = 1
p = 0
while True:
    p = i * i
    if p > n:
        break
    print(p, end=' ')
    i += 1