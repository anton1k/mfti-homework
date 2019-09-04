'''Для данной строки s найти строку p минимальной длины, такую что s можно предстваить как конкатенацию одной или нескольких копий p.t'''
def isInt(n):
    return int(n) == float(n)


def z_func(s, n):
    z = [0] * n
    y = 0
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min (r-i+1, z[i-l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i+z[i]-1 > r:
            l, r = i, i+z[i]-1
    for i in range(len(z)):
        if i + z[i] == n and isInt(n/i):
            y = i
    return z, y

s = 'abaababababababab'

print(z_func(s, len(s))[1])


