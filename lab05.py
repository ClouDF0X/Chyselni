import sympy as sp
import math

# Приклад використання
x_values = [2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6]  # Вузли
y_values = [3.526, 3.782, 3.945, 4.043, 4.104, 4.155, 4.222, 4.331, 4.507, 4.775, 5.159, 5.683]  # Значення функції у вузлах
x1 = [2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4]
x = [3.25, 3.36, 3.48, 3.63]


def create_difference_matrix(vector, a):
    matrix = []
    new_vector1 = []
    new_vector2 = []
    while len(vector) > 1:
        diff_column = [vector[i+1] - vector[i] for i in range(len(vector) - 1)]  # Обчислюємо різниці між сусідніми елементами
        matrix.append(diff_column)  # Додаємо різницю як новий стовпець матриці
        new_vector1.append(vector[0])
        new_vector2.append(vector[-1])
        vector = diff_column  # Оновлюємо вектор для наступної ітерації
    new_vector1.append(vector[0])  # Додаємо останній елемент у новий вектор
    new_vector2.append(vector[-1])
    if a == 1:
        return new_vector1
    else:
        return new_vector2


def newton_first(x, xi, yi, a):
    t = sp.Symbol('t')
    h = xi[1] - xi[0]
    n = len(xi)
    if a == 1:
        y1 = 1 / h
    else:
        y1 = 1/(h**2)
    all_diff = create_difference_matrix(yi, 1)
    t1 = (x - xi[0])/h
    y = 0
    for i in range(0, n-1):
        diff = all_diff[i+1]
        p = t
        for j in range(i):
            p = sp.expand(p * (t - (j + 1)))
            # print(p)
        # print(p)
        if a == 1:
            p = sp.diff(p, t)  # похідна
        else:
            p = sp.diff(p, t)  # похідна
            p = sp.diff(p, t)  # похідна
        # print(p)
        p = p.subs(t, t1)  # підстановку у похідну
        y += (diff*p) / (math.factorial(i))
    return y * y1


def newton_second(x, xi, yi, a):
    t = sp.Symbol('t')
    h = xi[1] - xi[0]
    n = len(xi)
    if a == 1:
        y1 = 1 / h
    else:
        y1 = 1 / (h ** 2)
    all_diff = create_difference_matrix(yi, 2)
    t1 = (x - xi[-1])/h
    y = 0
    for i in range(0, n-1):
        diff = all_diff[i+1]
        p = t
        for j in range(i):
            p = sp.expand(p * (t + (j + 1)))
            # print(p)
        # print(p)
        if a == 1:
            p = sp.diff(p, t)  # похідна
        else:
            p = sp.diff(p, t)  # похідна
            p = sp.diff(p, t)  # похідна
        # print(p)
        p = p.subs(t, t1)  # підстановку у похідну
        y += (diff * p) / (math.factorial(i))
    return y * y1

t = 1
print("Нютона:")
result_first1 = []
result_first2 = []
result_second1 = []
result_second2 = []
result_test1 = []
result_test2 = []
for i in x1:
    result_test1.append(newton_first(i, x_values, y_values, 1))
    result_test2.append(newton_first(i, x_values, y_values, 2))
print("------------------------------------------------")
for i in x:
    result_first1.append(newton_first(i, x_values, y_values, 1))
    print(f"Перша формула: f'(x{t}):", result_first1[t-1], end="\t")
    result_first2.append(newton_first(i, x_values, y_values, 2))
    print(f"f''(x{t}):", result_first2[t-1])
    result_second1.append(newton_second(i, x_values, y_values, 1))
    print(f"Друга формула: f'(x{t}):", result_second1[t-1], end="\t")
    result_second2.append(newton_second(i, x_values, y_values, 2))
    print(f"f''(x{t}):", result_second2[t-1])
    print("------------------------------------------------")
    t += 1

import matplotlib.pyplot as plt


def plot_graphs(*args):

    # Перевірка, що передано принаймні по одному списку значень ікса та ігрика
    if len(args) % 2 != 0:
        raise ValueError("Потрібно передати принаймні по одному списку значень ікса та ігрика.")

    # Побудова графіків
    for i in range(0, len(args), 2):
        x_values = args[i]
        y_values = args[i + 1]
        plt.plot(x_values, y_values)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Графіки функцій')
    plt.grid(True)
    plt.show()

# plot_graphs(x_values, y_values, x1, result_test1, x, result_first1, x, result_first2)
# plot_graphs(x_values, y_values, x1, result_test2, x, result_second1, x, result_second2)

