'''Саша, не сделал домашнюю работу, зато купил шоколадку. И, по глупости, начал распечатывать ее прямо на уроке... Шелест золотинки услышала учительница. Она хотела вызвать в школу родителей, но Саша уговорил ее не вызывать их, а дать дополнительное задание.

Учительница внимательно посмотрела на шоколадку (она была размером 3 на 4 плиток), разделила на кусочки по две плитки и угостила всех, кто сделал домашнюю работу. А Сашу попросила написать программу, которая определяет, сколько существует способов деления шоколадки размером 3 на N плиток на кусочки по две плитки.

Для выполнения задания Саше нужна помощь.

Примечание: все плитки в шоколадке пронумерованы, поэтому способы деления, симметричные относительно точки или оси могут будут разными.

Формат входных данных
На входе одно число N <= 10000

Формат выходных данных
Вывести одно число, количество способов разделить шоколадку.'''

n = int(input())
a, b, c = 1, 3, 0
if n%2 == 1:
    b = 0
else:
    for i in range(1, n//2):      
        c = 4*b - a
        a, b = b, c
print(b)