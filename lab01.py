# x^2 - 2cos(x) = 0

# === модулі які розв'язують рівняння і малюють графік (може потрібно буде для графіка) ===

# from scipy.optimize import fsolve
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Задана функція
# def equation(x):
#     return x**2 - 2*np.cos(x)
#
# # Визначення відрізка для пошуку кореня
# interval = np.linspace(-2, 2, 1000)
#
# # Побудова графіка функції
# plt.plot(interval, equation(interval), label='y = x^2 - 2cos(x)')
# plt.axhline(0, color='black', linewidth=0.5, linestyle='--', label='y = 0')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.grid(True)
# plt.show()
#
# # Пошук кореня на вказаному відрізку
# initial_guess = 0.5  # Початкове припущення для кореня
# root = fsolve(equation, initial_guess)
#
# print(f"Знайдений корінь: {root}")
# =======================================================

# === Модуль з уже готовою функцією ======================

# from scipy.optimize import bisect
# import numpy as np
#
#
# # Визначення функції
# def f(x):
#     return x ** 2 - 2 * np.cos(x)
#
#
# # Визначення відрізка [a, b]
# a = 0.0
# b = 2.0
#
# # Перевірка умови f(a) * f(b) < 0
# if f(a) * f(b) > 0:
#     print("Не виконується умова f(a) * f(b) < 0. Виберіть інший інтервал.")
# else:
#     # Знаходження кореня рівняння за допомогою методу бісекції
#     root = bisect(f, a, b)
#     print("Знайдений корінь рівняння:", root)
# # =========================================================
#
# # === Завдання 1 ==========================================
#
# from math import *
# import sympy as sp
#
# def f(x):
#     return x ** 2 - 2 * cos(x)
# #
# # # =============== Пошук можливиш меж =============
# # Пошук межі з лівої сторони початок
# def find_a_b(func, x_start, step=0.1):
#     a = x_start
#     b = x_start + step
#     while func(a) * func(b) > 0:  # Доки знаки однакові
#         b += step
#         if b > 100:
#             print("Виберіть іншу сторону")
#             return
#     return a, round(b, 5)
#
#
# # Межі з правої сторони початок
# def find_a_b_minus(func, x_start, step=0.1):
#     a = x_start
#     b = x_start - step
#     while func(a) * func(b) > 0:
#         b -= step
#         if b < -100:
#             print("Виберіть іншу сторону")
#             return
#     return round(b, 5), a
# # ===================================================
#
# start_x = float(input("Введіть початкове число межі: "))
# s = int(input("Введіть сторону (ліво - 1 \ право - 2): "))
# try:
#     if s == 1:
#         a, b = find_a_b_minus(f, start_x)
#     elif s == 2:
#         a, b = find_a_b(f, start_x)
#     else:
#         print("Не вірні дані")
#     print(a, b)
# except:
#     pass
#
# x = sp.symbols('x')
# # Визначення функції
# f = x**2 - 2 * sp.cos(x)
# # Перевірка чи не міняється знак похідної
# def test(f, a, b):
#     # Створення символьної змінної
#     global test2_result
#     t = 0
#     znak = True
#     for i in np.arange(a, b, 0.1):
#         # Обчислення похідної відносно x
#         f1 = sp.diff(f, x).subs(x, i)  # підстановка числа у похідну
#         t += 1
#         if t == 1:
#             znak = True if f1 < 0 else False  # якщо число від'ємне то True
#             continue
#         else:
#             znakt = True if f1 < 0 else False
#
#         if znakt != znak:
#             test2_result = False
#             break
#         test2_result = True
#     return test2_result
#
# test1_res = test(f, a, b)
# f1 = sp.diff(f, x)
# test2_res = test(f1, a, b)
# print("перша похідна = ", test1_res, "Друга похідна = ", test2_res)
# =====================================================================


from math import *

a = 0
b = 2
eps = 0.001


# Рівняння
def f(x):
    return x ** 2 - 2 * cos(x)


# Похідна
def f1(x):
    return (2 * x) + (2 * sin(x))


def hord(f, a, b, eps):
    t = 0
    while abs(f(a)) > eps:
        c1 = a - ((f(a) * (b - a)) / (f(b) - f(a)))
        a = c1
        t += 1
    return a, t


def dot(f, f1, b, eps):
    t = 0
    while abs(f(b)) > eps:
        d1 = b - (f(b) / f1(b))
        b = d1
        t += 1
    return b, t


def combined_method(f, f1, a, b, eps):
    t = 0
    while abs(f(b) - f(a)) > eps:
        d1 = b - (f(b) / f1(b))
        b = d1

        c1 = a - ((f(a) * (b - a)) / (f(b) - f(a)))
        a = c1

        t += 1
    x = (a + b) / 2
    return x, t

# з більшою точністю значення подібне на інші варіанти
def half(f, a, b, eps):
    t = 0
    while abs((b - a)/2) > eps:
        c1 = (a + b) / 2
        if f(c1) == 0:
            return c1, t
        elif f(c1) * f(a) < 0:
            b = c1
        else:
            a = c1
        t += 1
    return (a + b)/2, t

def g(x):
    return sqrt(2*cos(x))
def iterations(f, eps, x0 = 1):
    x = x0
    t = 0
    while True:
        t += 1
        xn = f(x)
        if abs(xn - x) < eps:
            return xn, t
        x = xn

print("Метод Хорд: ", hord(f, a, b, eps))
print("Метод Дотичних: ", dot(f, f1, b, eps))
print("Комбінований метод: ", combined_method(f, f1, a, b, eps))
print("Метод половинного поділу: ", half(f, a, b, eps))
print("Метод простої ітерації: ", iterations(g, eps))