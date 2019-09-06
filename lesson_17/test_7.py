'''В файле task6/en-ru.txt находятся строки англо-русского словаря в таком формате:

cat - кошка
dog - собака
home - домашняя папка, дом
mouse - мышь, манипулятор мышь
to do - делать, изготавливать
to make - изготавливать
Здесь английское слово (выражение) и список русских слов (выражений) разделены двумя табуляциями и минусом: '\t-\t'.

Требуется создать русско-английский словарь и вывести его в файл ru-en.txt в таком формате:

делать - to do
дом - home
домашняя папка - home
изготавливать - to do, to make
кошка - cat
манипулятор мышь - mouse
мышь - mouse
собака - dog
Порядок строк в выходном файле должен быть словарным с человеческой точки зрения (так называемый лексикографический порядок слов). То есть выходные строки нужно отсортировать.'''

left = set() #чтобы слова не повторялись
dictionary = {}

# чтение из файла
with open('en-ru7.txt', encoding='utf-8') as f:
    for line in f:
        line = line.split('\t-\t')
        line[1] = line[1].strip(',=\n-')
        left.add(line[1])
        dictionary[line[1]] = line[0]

# преобразование в массив и сортировка
right = list(left)
right = sorted(right)

# убрал какой то мусор
for i in range(len(right)):
    if right[i] == 'Авадон':
        right = right[i:]
        break

# запись в файл
with open('ru-en7.txt', 'a', encoding='utf-8') as r:
    for rus in right:
        s =  rus + '\t-\t' + dictionary[rus] + '\n'
        r.write(s)

