'''Герою компьютерной игры нужно перебраться от одного края экрана к другому, перепрыгивая по платформам. При этом при прыжке с одной платформы на соседнюю, у героя уходит |y2-y1| единиц энергии, где y1 и y2 – высоты, на которых расположены эти платформы. Кроме того, у героя есть суперприем, который позволяет перескочить через платформу, но на это затрачивается 3*|y3-y1| единиц энергии. Конечно же, энергию следует расходовать максимально экономно.

Вам известны высоты всех платформ в порядке от левого края до правого. Необходимо найти, какое минимальное количество энергии потребуется герою, чтобы добраться с первой платформы до последней.

Формат входных данных
В первой строке - количество платформ (0 < n <= 30000). Далее на каждой из n строк записана высота , на которой расположена очередная платформа.

Формат выходных данных
Одно число — минимальное количество энергии, которую должен потратить герой на преодоление платформ.'''

n = int(input())
arr = [0]*n

for i in range(n):
    arr[i] = int(input())

def prices(arr, n):
    price = [0, abs(arr[1] - arr[0]) if n > 1 else 0]

    for i in range(2, n):
        price.append((min(
            abs(arr[i]-arr[i-1]) + price[i-1],
            3*abs(arr[i]-arr[i-2]) + price[i-2]
            )))

    return price[n-1] if n > 1 else price[0]

print(prices(arr, n))

