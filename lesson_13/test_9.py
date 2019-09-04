'''Для данной строки s найти строку p минимальной длины, такую что s можно предстваить как конкатенацию одной или нескольких копий p. Используйте префикс-функцию.'''
def isInt(n):
    return int(n) == float(n)

def p_func(s, n):
	pi = [0]*n
	res = n
	for i in range(1, n):
		j = pi[i-1]
		while j > 0 and s[i] != s[j]:
			j = pi[j-1]
		if s[i] == s[j]:
			 j += 1
		pi[i] = j
	k = n - pi[n-1]

	if isInt(n/k):
		res = n/k

	return pi, res

s = 'aaaaaabaaa'

print(p_func(s, len(s)))

