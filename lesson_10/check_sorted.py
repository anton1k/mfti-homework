import util
import quick_sort
import merge_sort
import bubble_sort

util.plot_sort_results(
    ('Быстрая сортировка: произвольный элемент в качестве опорного', quick_sort.quick_sort_random),
    ('Сортировка слиянием', merge_sort.merge_sort),
    ('Сортировка пузырьком: обычная реализация', bubble_sort.bubble_sort),
)
util.plot_sort_results(
    ('Быстрая сортировка: первый элемент в качестве опорного', quick_sort.quick_sort_first),
    ('Сортировка слиянием', merge_sort.merge_sort),
    ('Сортировка пузырьком: пеализация с проверкой на отсортированность', bubble_sort.bubble_sort_adaptive),
)