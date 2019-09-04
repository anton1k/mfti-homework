import util

# числа фибаначи

# рекурсивное вычесление
def recursive_fib(n):
    return n if n < 2 else recursive_fib(n-1) + recursive_fib(n-2)

# рекурсивное вычесление, но с дополнительным массивом в роли кеша
def recursive_fib_with_cache(n, cache=None):
    cache = cache or ([0, 1] + [-1] * (n-1))
    if cache[n] == -1:
        cache[n] = recursive_fib_with_cache(n-1, cache) + recursive_fib_with_cache(n-2, cache)
    
    return cache[n]

# нерекурсивной выполнение
def fib(n):
    if n < 2:
        return n
    
    a, b = 1, 1

    for i in range(2, n+1):
        a, b = b, a + b
    
    return a

# проверим скорость работы
util.plot_fib_results(
    ('Рекурсивная реализация', recursive_fib),
    ('Рекурсивная реализация с кешем', recursive_fib_with_cache),
    ('Рекурсивная при помощи цикла', fib)
)