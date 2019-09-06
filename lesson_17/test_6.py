'''Дан список стран и языков на которых говорят в этой стране в формате <Название Страны> : <язык1> <язык2> <язык3> ... в файле task5/input.txt. На ввод задается N - длина списка и список языков. Для каждого языка укажите, в каких странах на нем говорят'''

# N = int(input())
# language = {}

# for i in range(N):
#     language[input()] = []

language = {
    'русский' : [],
    'малагасийский' : [],
    'французский' : []
}
dictionary = {}

# чтение списка стран и языков
with open('input6.txt', encoding='utf-8') as f:
    for line in f:
        line = line.split(':')
        country = line[0]
        lang = line[1].split()
        dictionary[country] = lang


# сравнение
for key, value in dictionary.items():
    for l in language:
        if l in value:
            language[l].append(key)

# вывод
for key, value in language.items():
    print(key, ':', ', '.join(value))

