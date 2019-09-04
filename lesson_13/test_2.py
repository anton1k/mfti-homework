'''Пусть даны две строки. Найти все вхождения второй строки в первую.'''

def z_func(t, p, n):
    s = t + '#' + p
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min (r-i+1, z[i-l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i+z[i]-1 > r:
            l, r = i, i+z[i]-1
    
    for i in range(0, len(t)-1):
        if z[i + len(p) + 1] == len(p):
            print('Yes')
    return z

s = 'aaaabaa'
p = 'aaaav'
print(z_func(s, p, len(s) + len(p) + 1))
