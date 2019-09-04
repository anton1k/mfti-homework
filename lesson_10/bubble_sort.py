import util

# сортировка пузырьком
def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


# улучшенная реализайция сортировки пузырьком
def bubble_sort_adaptive(a):
    n = len(a)
    for i in range(n-1):
        swaped = False
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaped = True
            if not swaped:
                break

# проверка скорости работы
# util.plot_bubble_sort_results(
#     ('Обычная реализация', bubble_sort),
#     ('Реализация с проверкой на отсортированность', bubble_sort_adaptive),
# )