from math import *

# Варіант 17

# === 1 ===
def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# def area(x1, y1, x2, y2, x3, y3):
#     a = distance(x1, y1, x2, y2)
#     b = distance(x2, y2, x3, y3)
#     c = distance(x3, y3, x1, y1)
#
#     s = (a + b + c) / 2
#
#     S = sqrt(s * (s - a) * (s - b) * (s - c))
#
#     return S
#
# x1, y1 = map(float, input("(x1 y1): ").split())
# x2, y2 = map(float, input("(x2 y2): ").split())
# x3, y3 = map(float, input("(x3 y3): ").split())
#
# print(round(area(x1, y1, x2, y2, x3, y3), 5))

# === 2 ===

# x = float(input("Введіть Х: "))
# if x <= 0:
#     a = 0
# elif 0 < x <= 1:
#     a = (x**2)*x
# else:
#     a = (x**2) - (sin(pi*(x**2)))
# print("f(x) = ", a)

# === 3.17 ===

# def find_n(a):
#     if a == 0:
#         return 0
#     sum = 0  # сума зліва
#     n = 1
#
#     while sum <= a:  # чи сума не більша за а
#         sum += 1/n
#         n += 1
#
#     return n - 1
#
# a = float(input("Введіть число a: "))
#
# result_n = find_n(a)
#
# print(f"Найменше n = {result_n}")

# === 3.27 ===

# n = int(input("Введіть n: "))
# k = 1
# sum = 0
# for i in range(n):
#     sum += 1/(k**5)
#     k += 1
# print(sum)

# === 4.1(7) ===
# def remove_groups(input_string):
#     result = input_string
#     while 'abcd' in result:
#         result = result.replace('abcd', '')
#     return result
#
# input_str = input("Введіть рядок: ")
# output_str = remove_groups(input_str)
# print(output_str)

# === 4.2(18d) ===

# def count_words(input_string):
#     words = input_string.split()  # розділити рядок на слова
#     count = 0
#
#     for word in words:
#         if len(word) >= 2 and word[0] == word[-1]:
#             count += 1
#
#     return count
#
# input_str = input("Введіть рядок: ")
# result = count_words(input_str)
# print(f"Кількість слів, у яких перший і останній символи співпадають: {result}")

# === 4.3(2d) ===

# def replace_dots(input_string):
#     result = ''
#     i = 0
#     while i < len(input_string):
#         # Знаходимо групу крапок
#         if input_string[i] == '.':
#             count_dots = 0
#             while i < len(input_string) and input_string[i] == '.':
#                 count_dots += 1
#                 i += 1
#             # Замінюємо групу крапок на три крапки
#             result += '...' if count_dots > 1 else '.'
#         else:
#             result += input_string[i]
#             i += 1
#
#     return result
#
# input_str = input("Введіть рядок: ")
# output_str = replace_dots(input_str)
# print(output_str)


