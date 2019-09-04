import util
import random

# быстрая сортировка

# реализация с первым элеменотом массива в качестве опорного
def quick_sort_first(a):
    if len(a) <= 1:
        return
    
    pivot = a[0]

    l, m, r = [], [], []

    for x in a:
        if x < pivot:
            l.append(x)
        elif x > pivot:
            r.append(x)
        else:
            m.append(x)

    quick_sort_first(l)
    quick_sort_first(r)

    for i, x in enumerate(l + m + r):
        a[i] = x

# реализация с средним элементом массива в качестве опорного
def quick_sort_middle(a):
    if len(a) <= 1:
        return
    
    pivot = a[len(a)//2]

    l, m, r = [], [], []

    for x in a:
        if x < pivot:
            l.append(x)
        elif x > pivot:
            r.append(x)
        else:
            m.append(x)

    quick_sort_middle(l)
    quick_sort_middle(r)

    for i, x in enumerate(l + m + r):
        a[i] = x

# реализация с произвольным элементом массива в качестве опорного
def quick_sort_random(a):
    if len(a) <= 1:
        return
    
    pivot = random.choice(a)

    l, m, r = [], [], []

    for x in a:
        if x < pivot:
            l.append(x)
        elif x > pivot:
            r.append(x)
        else:
            m.append(x)

    quick_sort_random(l)
    quick_sort_random(r)

    for i, x in enumerate(l + m + r):
        a[i] = x

# util.plot_quick_sort_results(
#     ('Первый элемент в качестве опорного', quick_sort_first),
#     ('Средний элемент в качестве опорного', quick_sort_middle),
#     ('Произвольный элемент в качестве опорного', quick_sort_random)
# )