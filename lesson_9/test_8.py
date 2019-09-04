'''Напечатайте входную последовательность натуральных чисел, отсортировав ее по возрастанию сначала единиц, потом десятков, потом сотен и тп.
Входные данные
Целое число 0 < N ≤ 1000. Затем N натуральных чисел, не превышающих 30000, через пробел.
Выходные данные
Числа по возрастанию единиц, при равных единиц - по возрастанию десятков, при равных единицах и десятков - по возрастанию сотен и тп.'''

import random

n = int(input())
s = input().split()

nums = [int(x) for x in s]

def quick_sort_middle(a, step):
    if len(a) <= 1:
        return
    pivot = random.choice(a)
    l = []
    m = []
    r = []
    for x in a:
        if x%step < pivot%step:
            l.append(x)
        elif x%step > pivot%step:
            r.append(x)
        else:
            m.append(x)
    quick_sort_middle(l, step)
    quick_sort_middle(r, step)

    for i, x in enumerate(l + m + r):
        a[i] = x

quick_sort_middle(nums, 1000)
quick_sort_middle(nums, 100)
quick_sort_middle(nums, 10)

print(' '.join(str(x) for x in nums))

# РАБОТАЕТ НО ДОЛГО
# n = int(input())
# s = input().split()

# s = [int(x) for x in s]

# for i in range(n-1):
#     for j in range(n-i-1):
#         if s[j]%1000 > s[j+1]%1000:
#             s[j], s[j+1] = s[j+1], s[j]

# for i in range(n-1):
#     for j in range(n-i-1):
#         if s[j]%100 > s[j+1]%100:
#             s[j], s[j+1] = s[j+1], s[j]

# for i in range(n-1):
#     for j in range(n-i-1):
#         if s[j]%10 > s[j+1]%10:
#             s[j], s[j+1] = s[j+1], s[j]

# print(' '.join(str(x) for x in s))
