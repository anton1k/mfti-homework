'''
Даны координаты точки и радиус круга с центром в начале координат. Определить, принадлежит ли данная точка кругу. Напомним, что круг – это часть плоскости, состоящая из всех точек окружности и всех точек, лежащих внутри окружности.
'''

import math
import re

n = input()

res = re.findall('\d+', n)

r_xy = math.sqrt(int(res[0])**2 + int(res[1])**2)

print("YES" if r_xy <= int(res[2]) else "NO")