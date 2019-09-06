'''Даны два файла словарей: task7/en-ru.txt и task7/ru-en.txt (в формате, описанном в упражнении №6).

en-ru.txt:

home - домашняя папка
mouse - манипулятор мышь
ru-en.txt:

дом - home
мышь - mouse
Требуется синхронизировать и актуализировать их содержимое.

en-ru.txt:

home - домашняя папка, дом
mouse - манипулятор мышь, мышь
ru-en.txt:

дом - home
домашняя папка - home
манипулятор мышь - mouse
мышь - mouse'''

#чтобы слова не повторялись
sort = set()
sort1 = set()

dictionary = {}
dictionary1 = {}

outdictionary = {}
outdictionary1 = {}
# чтение из файла
with open('en-ru8.txt', encoding='utf-8') as f:
    for line in f:
        line = line.split('\t-\t')
        line[1] = line[1].strip(',=\n-')
        sort.add(line[0])
        dictionary[line[0]] = line[1].split(',')

# чтение из файла
with open('ru-en8.txt', encoding='utf-8') as f:
    for line in f:
        line = line.split('\t-\t')
        line[1] = line[1].strip(',=\n-')
        sort1.add(line[0])
        dictionary1[line[0]] = line[1].split(',')

# обоьединение словарей en-ru и ru-en
for key, value in dictionary1.items():
    for i in value:
        if i in dictionary: 
            dictionary[i].append(key) 

# обоьединение словарей ru-en и en-ru 
for key, value in dictionary.items():
    for i in value:
        if i in dictionary1: 
            dictionary1[i].append(key) 


# преобразование в массив и сортировка
sort = list(sort)
sort1 = list(sort1)
sort = sorted(sort)
sort1 = sorted(sort1)

# убрал какой то мусор
for i in range(len(sort1)):
    if sort1[i] == 'Авадон':
        sort1 = sort1[i:]
        break

# запись в файл
with open('en-ru8out.txt', 'a', encoding='utf-8') as r:
    for en in sort:
        s =  en + '\t-\t' + ', '.join(dictionary[en]) + '\n'
        r.write(s)

# запись в файл
with open('ru-en8out.txt', 'a', encoding='utf-8') as r:
    for rus in sort1:
        s =  rus + '\t-\t' + ', '.join(dictionary1[rus]) + '\n'
        r.write(s)


