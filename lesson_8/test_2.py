'''Напишите программу, вычисляющую n-ное число Фибоначчи. Используйте рекурсивные вызовы функций.'''
# Ввод	Вывод
#  7	 13

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
 
print(fibonacci(7))