# Реализовать стековый калькулятор на python. Написать программу, которая читает выражение в обратной польской нотации и считает его значение или пишет, что выражение составлено не корректно (если оно некорректно).

import test_1 as A_stack # импотритрует наш собственный модуль стек из файлв test_1.py

def postfixEval(postfixExpr): # принисмет строку введеную через пробел, что бы принимало строку без пробелов, то tokenList = postfixExpr.split() нужно заменить на tokenList = list(postfixExpr)
    tokenList = postfixExpr.split()
    try:
        for token in tokenList:
            if token in "0123456789":
                A_stack.push(int(token))
            else:
                operand2 = A_stack.pop()
                operand1 = A_stack.pop()
                result = doMath(token,operand1,operand2)
                A_stack.push(result)
    except:
        return 'Вы что-то ввели не правильно'
    return A_stack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))