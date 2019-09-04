'''Напишите префикс-функцию. Пусть заголовком ее будет def p_func(s, n):'''


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

print(p_func(s, len(s)))

