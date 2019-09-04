'''Входные данные
Слово в алфавите из двух круглых скобочек ( и ). Длина слова меньше 4001
Выходные данные
Либо NO, либо YES'''

s = input()

def fun(s):
    t = 0
    for i in range(len(s)):
        if s[i] == ')' and t <= 0:
            return 'NO'
        if s[i] == '(':
            t += 1
        if s[i] == ')':
            t -= 1
    return 'YES' if t == 0 else 'NO'
    
print(fun(s))