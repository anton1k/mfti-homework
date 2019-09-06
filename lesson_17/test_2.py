# Вывести на экран все элементы множества A, которых нет в множестве B.
A = set('bqlpzlkwehrlulsdhfliuywemrlkjhsdlfjhlzxcovt')
B = set('zmxcvnboaiyerjhbziuxdytvasenbriutsdvinjhgik')
for x in A:
    if x not in B:
        print(x, end=', ') #в одну строку через запятую