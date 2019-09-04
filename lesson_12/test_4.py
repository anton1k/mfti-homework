'''Написать функцию make_exchange(money, coins), которая принимает сумму денег (целое число) и массив номиналов разменных монет (целых чисел) (возможно пустой) и возвращает количество способов произвести размен. Считаем, что разменных монет бесконечное множество.

Формат выходных данных
Число способов произвести размен. Способы 1+2 и 2+1 считаем тождественными.'''



def make_exchange(target, coins):
    combinations = [0]*(target + 1)
    combinations[0] = 1

    for coin in coins:
        for i in range(1, target+1):
            if i >= coin:
                combinations[i] = combinations[i] + combinations[i - coin]

    return combinations[target]


print(make_exchange(10, [5,2,3]))