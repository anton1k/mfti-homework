'''В одном очень дружном доме, где живет Фёдор, многие жильцы оставляют ключи от квартиры соседям по дому, например на случай пожара или потопа, да и просто чтобы покормили животных или полили цветы.

Вернувшись домой после долгих странствий, Фёдор обнаруживает, что потерял свои ключи и соседей дома нет. Но вдруг у домофона он находит чужие ключи. Помогите Федору найти ключи от своей квартиры в квартирах соседей.

На ввод подается файл input.txt, в котором в первой строке записано три числа через пробел N - номер квартиры Фёдора, M - номер квартиры от которой Федор нашел ключи, K - ключ от этой квартиры. Далее i-я строка хранит описание ключей запертых в i-й квартире в формате <m_i0 - номер квартиры> <k_i0 - ключ>,<m_i1 - номер квартиры> <k_i1 - ключ>,... , причем реальные номера квартир "зашифрованы" ключем от i-й квартиры(Ki) и находятся по формуле m_ij' = m_ij - Ki. Номера квартир начинаются с 0 (кпримеру вторая строка файла соответствует 0-й квартире).

Нужно вывести ключ от квартиры Федора или None если его найти не получилось.'''

from random import randrange
from random import choice

nk = list(map(int, input().split()))
N, K = nk[0], nk[1]
keys = []
neighs = []
key_store = [None] * N

for i in range(N):
    # Зададим ключ для квартиры
    keys.append(randrange(N//4+1))

    # Зададим количество соседей у которых есть ключ
    n_neigh = randrange(1, K+1)

    # Сгенерим номера соседей
    neighs.append([])
    for j in range(n_neigh):
        neighs[i].append(randrange(N))

    # Дадим соседям ключи
    for j in range(n_neigh):
        if not key_store[neighs[i][j]]:
            key_store[neighs[i][j]] = []
        key_store[neighs[i][j]].append([i, keys[i]])

# Выберем квартиру Фёдора
N0 = randrange(N)
# Найдем всех соседей от которых можно придти в квартиру Фёдора
old = set()
new = {N0}
while len(new):
    i = new.pop()
    old.add(i)
    for j in range(len(neighs[i])):
        if neighs[i][j] not in old:
            new.add(neighs[i][j])
# Выберем одного
M0 = choice(list(old))

print('#########')
print('Ответ:', keys[N0])
print('#########')

f = open('input.txt', 'w')
print("N =", N0, "M =", M0, "K =", keys[M0])
print(N0, M0, keys[M0], file = f)
for i in range(N):
    if not key_store[i]:
        key_store[i] = []

    print(str(i) + ' : ', end = '')

    for j in range(len(key_store[i])):
        # "Запрем" дверь
        key_store[i][j][0] += keys[i]

        end = ','
        if j == len(key_store[i]) - 1:
            end = ''
        print(key_store[i][j][0], key_store[i][j][1], end = end)
        print(key_store[i][j][0], key_store[i][j][1], end = end, file = f)
    print()
    print(file = f)