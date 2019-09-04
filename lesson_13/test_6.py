'''Пусть даны две строки. Найти все вхождения второй строки в первую с помощью алгоритма Кнута-Морриса-Пратта.'''


def p_func(t, p, n):
	s = t + '#' + p
	pi = [0]*n
	res = []
	for i in range(1, n):
		j = pi[i-1]
		while j > 0 and s[i] != s[j]:
			j = pi[j-1]
		if s[i] == s[j]:
			 j += 1
		pi[i] = j

	for i in range(len(t)+1):
		if pi[i] == len(p):
			res.append(i)
	
	return pi, res


t = 'aaaaabaa'
p = 'aab'

print(p_func(t, p, len(t) + len(p) + 1))
