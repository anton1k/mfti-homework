'''Еривиальные алгоритмы'''

def z_func(s, n):
    z = [0] * n
    for i in range(1, n - 1):
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
    return z

s = 'aaaabaa'

print(z_func(s, len(s)))


def prefix_func(s, n):
    pi = [0] * n
    for i in range(n - 1):
        for k in range(1, i + 1):
            equal = True
            for j in range(k):
                if s[j] != s[i - k  + 1 + j]:
                    equal = False
                    break
            if equal:
                pi[i] = k
    return pi


print(prefix_func(s, len(s)))
