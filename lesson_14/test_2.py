# Написать программу, определяющую правильность введенного скобочного выражения, в котором используются скобки 3 видов: (), {}, []

import test_1 as A_stack # импотритрует наш собственный модуль стек из файлв test_1.py

def is_braces_sequence_correct(s:str):
    '''
    Проверяет корректоность скобочной последовательности из скобок () [] {}
    >>> is_braces_sequence_correct('({[]})')
    True
    >>> is_braces_sequence_correct('({(([]))})')
    True
    >>> is_braces_sequence_correct('{[]})')
    False
    >>> is_braces_sequence_correct('({[]}')
    False
    >>> is_braces_sequence_correct('{}[](')
    False
    >>> is_braces_sequence_correct('[[))')
    False
    '''
    for brace in s:
        if brace not in '(){}[]':
            continue
        if brace in '([{':
            A_stack.push(brace)
        else:
            assert brace in ')}]', 'Ожидалась закрывающая скобка: ' + str(brace)
            if A_stack.is_empty():
                return False
            left = A_stack.pop()   
            assert left in '([{', 'Ожидалась открывающая скобка: ' + str(brace)
            if left == '(':
                right = ')'
            elif left == '[':
                right = ']'
            elif left == '{':
                right = '}'
            if right != brace:
                return False

    return A_stack.is_empty()


if __name__ == '__main__':
    import doctest  # тестирование
    doctest.testmod() # verbose=True/False - показать результаты тестирование
    


