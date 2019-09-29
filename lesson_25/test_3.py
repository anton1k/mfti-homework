# В Банановой республике очень много холмов, соединенных мостами. На химическом заводе произошла авария, 
# в результате чего испарилось экспериментальное удобрение зован. На следующий день выпал цветной дождь, 
# причем он прошел только над холмами. В некоторых местах падали красные капли, в некоторых – синие, а в 
# остальных – зеленые, в результате чего холмы стали соответствующего цвета. Президенту Банановой 
# республики это понравилось, но ему захотелось покрасить мосты между вершинами холмов так, чтобы мосты 
# были покрашены в цвет холмов, которые они соединяют. К сожалению, если холмы разного цвета, то 
# покрасить мост таким образом не удастся. Посчитайте количество таких плохих мостов.


# N = 7
# m = [['0', '1', '0', '0', '0', '1', '1'], ['1', '0', '1', '0', '0', '0', '0'], ['0', '1', '0', '0', '1', '1', '0'], ['0', '0', '0', '0', '0', '0', '0'], ['0', '0', '1', '0', '0', '1', '0'], ['1', '0', '1', '0', '1', '0', '0'], ['1', '0', '0', '0', '0', '0', '0']]
# s = ''
# color = ['1', '1', '1', '1', '1', '3', '3']

N = int(input())
m = [ input().split() for i in range(N)]
s = input()
color = input().split() 
count = 0


for i in range(N):
    for j in range(i+1, N):
        # Проверка наличия моста между холмами
        if int(m[i][j]):
        # Проверка цвета холмов
            if (color[i] != color[j]):
                count += 1

print(count)


