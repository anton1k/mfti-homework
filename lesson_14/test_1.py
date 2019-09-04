# Напишите программу, которая последовательно кладет в стек произвольный массив чисел, а затем распечатывает их , последовательно доставая, пока стек не пуст (например, набор (1,...,10)).

'''Модуль стек

>>> clear()
>>> is_empty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> is_empty()
False
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> is_empty()
True
'''

_stack = []

def push(x):
    _stack.append(x)

def pop():
    return _stack.pop()

def clear():
    _stack.clear()

def is_empty():
    return len(_stack) == 0

# if __name__ == '__main__':
#     import doctest  # тестирование
#     doctest.testmod() # verbose=True/False - показать результаты тестирование