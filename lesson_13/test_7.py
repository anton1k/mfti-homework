# В первой строке ввода - число n, количество букв в паттерне. Во второй строке - паттерн, строка которую нужно искать в тексте. В каждой из последующих строк - символы текста, по одному в каждой строке. Необходимо вывести позиции вхождений паттерна в текст. Длина текста заранее не известна, он может быть очень большим

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
p = ''
n = int(input())

for _ in range(n):
	p += input()

print(p_func(t, p, len(t) + len(p) + 1))

