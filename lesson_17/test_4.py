# Дан текст на некотором языке. Требуется подсчитать сколько раз каждое слово входит в этот текст и вывести десять самых часто употребяемых слов в этом тексте и количество их употреблений.

import string

count = 10 #сколько вывести результатов
vocabulary = {}

f = open('LICENSE.txt')
stringIn = f.read()
stringIn = "".join(l for l in stringIn if l not in string.punctuation)
arrStr = stringIn.split()

for s in arrStr:
    s = s.lower()
    try:
        vocabulary[s] += 1
    except KeyError:
        vocabulary[s] = 0

max_val = sorted(vocabulary.values(), reverse=True)

for i in range(count):
    for key, values in vocabulary.items():
        if max_val[i] == values:
            print(key, values)

