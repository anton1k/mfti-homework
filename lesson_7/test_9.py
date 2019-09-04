# Вам необходимо написать программу, которая в данном потоке чисел заранее неизвестной длины находит максимальное значение, отбрасывая при этом последние 5 измерений.

# Формат входных данных
# На вход вашей программе передается последовательность натуральных чисел -- результаты измерений. Каждое новое число передается с новой строки. Гарантируется, что длина входной последовательности не меньше 6 и не превосходит 10 9 . На конце последовательности передается число 0.

# Формат выходных данных
# Программа должна вывести на экран одно число  максимальное значение входной последовательности за исключением последних 5 элементов.

arr = []
maxsimum = 0

while True:
    x = int(input())
    if x == 0:
        break
    arr.append(x)
    if len(arr) > 5:
        if arr[0] > maxsimum:
            maxsimum = arr[0]
        del arr[0]

print(maxsimum)


# arr = []
# maxsimum = 0
# while True:
#     x = int(input())
#     if x == 0 or len(arr) > 10**9:
#         break
#     arr.append(x)
#     if len(arr) > 5:
#         if arr[len(arr)-6] > maxsimum:
#             maxsimum = arr[len(arr)-6]

# print(maxsimum)



# arr = []
# while True:
#     x = int(input())
#     if x == 0 or len(arr) > 10**9:
#         break
#     arr.append(x)

# print(max(arr[:-5]))

# arr = []
# while True:
#     x = int(input())
#     if x == 0 or len(arr) > 10**9:
#         break
#     arr.append(x)

# maximum = arr[0]
# for i in range(1, len(arr)-5):
#     if arr[i] > maximum:
#         maximum = arr[i]
# print(maximum)

# arr = []
# while True:
#     x = int(input())
#     if x == 0 or len(arr) > 10**9:
#         break
#     arr.append(x)

# new_arr = arr[:-5]
# new_arr.sort()
# print(new_arr[-1])

# arr = []
# while True:
#     x = int(input())
#     if x == 0 or len(arr) > 10**9:
#         break
#     arr.append(x)

# new_arr = arr[:-5]
# new_arr.sort()
# print(new_arr[-1])