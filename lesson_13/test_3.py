'''Найти число всех различных подстрок входящих в данную.'''
# так и не понял эту задачу
def z_func(t, n):
    z = [0] * n
    s = t + 'c'
    l, r = 0, 0
    s = s[::-1]
    for i in range(1, n):
        if i <= r:
            z[i] = min (r-i+1, z[i-l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i+z[i]-1 > r:
            l, r = i, i+z[i]-1
    return len(s) - max(z)

s = 'aaaabaa'

print(z_func(s, len(s)))
