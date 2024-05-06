"""

Варіант 17

Завдання 1:
Для 1
X: 0.68, 0.73, 0.8, 0.88, 0.93, 0.99
Y: 0.80866, 0.89492, 1.02964, 1.20966, 1.34087, 1.52368

x = 0.774

Для 2
X: 0.210, 0.215, 0.220, 0.225, 0.230, 0.235
Y: 4.83170, 4.72261, 4.61855, 4.51919, 4.42422, 4.33337

x = 0.2232

Завдання 2:
X: 1.340, 1.345, 1.350, 1.355, 1.360, 1.365, 1.370, 1.375, 1.380, 1.385, 1.390, 1.395
Y: 4.25562, 4.35325, 4.45522, 4.56184, 4.67344, 4.79038, 4.91306, 5.04192, 5.17744, 5.32016, 5.47069, 5.62968

x1 = 1.3463
x2 = 1.3868
x3 = 1.335
x4 = 1.3990
"""


def lagrange_interpolation(nodes, values, x):
    n = len(nodes)
    result = 0
    for i in range(n):
        term = values[i]
        for j in range(n):
            if j != i:
                term *= (x - nodes[j]) / (nodes[i] - nodes[j])
        result += term
    return result


# Приклад використання для нерівновіддалених вузлів
nodes_non_uniform = [0.68, 0.73, 0.8, 0.88, 0.93, 0.99]
values_non_uniform = [0.80866, 0.89492, 1.02964, 1.20966, 1.34087, 1.52368]
x_value = 0.774
result_non_uniform = lagrange_interpolation(nodes_non_uniform, values_non_uniform, x_value)
print("Лангранжа для нерівновіддалених вузлів:", result_non_uniform)


nodes = [0.210, 0.215, 0.220, 0.225, 0.230, 0.235]
values = [4.83170, 4.72261, 4.61855, 4.51919, 4.42422, 4.33337]
x = 0.2232
result = lagrange_interpolation(nodes, values, x)
print("Лангранжа для рівновіддалених вузлів:", result)

# Приклад використання
x_values = [1.340, 1.345, 1.350, 1.355, 1.360, 1.365, 1.370, 1.375, 1.380, 1.385, 1.390, 1.395]  # Вузли
y_values = [4.25562, 4.35325, 4.45522, 4.56184, 4.67344, 4.79038, 4.91306, 5.04192, 5.17744, 5.32016, 5.47069, 5.62968]  # Значення функції у вузлах

x = [1.3463, 1.3868, 1.335, 1.3990]


import math

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


def newton_first(x, xi, yi):
    h = xi[1] - xi[0]
    n = len(xi)
    y = yi[0]
    all_diff = create_difference_matrix(yi, 1)
    print(all_diff)
    for i in range(1, n):
        diff = all_diff[i]
        p = 1
        for j in range(i):
            p *= (x - xi[j])
        y += (diff*p) / (math.factorial(i)*(h**i))
    return y

def newton_second(x, xi, yi):
    h = xi[1] - xi[0]
    n = len(xi)
    y = yi[-1]
    all_diff = create_difference_matrix(yi, 2)
    for i in range(1, n):
        diff = all_diff[i]
        p = 1
        for j in range(i):
            p *= (x - xi[n-1-j])
        y += (diff*p) / (math.factorial(i) * (h**i))
    return y

t = 1
print("")
for i in x:
    result_first_form = newton_first(i, x_values, y_values)
    print(f"Ньютона за першою формулою(x{t}):", result_first_form)
    result_second_form = newton_second(i, x_values, y_values)
    print(f"Ньютона за другою формулою(x{t}):", result_second_form)
    print("")
    t += 1