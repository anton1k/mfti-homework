'''Найти число всех различных подстрок входящих в данную с помощью префикс-функции.'''
# так и не понял эту задачу

def p_func(s, n):
	pi = [0]*n
	for i in range(1, n):
		j = pi[i-1]
		while j > 0 and s[i] != s[j]:
			j = pi[j-1]
		if s[i] == s[j]:
			 j += 1
		pi[i] = j
	return pi


s = 'aaaaaabaaa'
res1 = p_func(s, len(s))

s += 'c'
s = s[::-1]

res2 = p_func(s, len(s))

print(len(s)-max(res1))


