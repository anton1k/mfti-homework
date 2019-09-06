'''Дан словарь task4/en-ru.txt с однозначным соответствием английских и русских слов в таком формате:

cat - кошка

dog - собака

mouse - мышь

house - дом

eats - ест

in - в

too - тоже

Здесь английское и русское слово разделены двумя табуляциями и минусом: '\t-\t'.

В файле task4/input.txt дан текст для перевода, например:

Mouse in house. Cat in house.
Cat eats mouse in dog house.
Dog eats mouse too.
Требуется сделать подстрочный перевод с помощью имеющегося словаря и вывести результат в output.txt. Незнакомые словарю слова нужно оставлять в исходном виде.'''

import string

vocabulary = {}

f = open('en-ru.txt', encoding='utf-8')

for line in f:
    translate = line.split()
    vocabulary[translate[0]] = translate[2]

f = open('input.txt')
for line in f:
    line = "".join(l for l in line if l not in string.punctuation)
    translate = line.lower().split()
    for i in range(len(translate)):
        try:
            translate[i] = vocabulary[translate[i]]
        except KeyError:
            continue
    translate = ' '.join(translate)
    t = open('output.txt', 'a', encoding='UTF-8')
    t.write(translate)
    t.close()

