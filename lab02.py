import copy

# Варіант 17
# Формула
"""

x1 - 4x2 - x4 = 2
x1 + x2 + 2x3 + 3x4 = 1
2x1 + 3x2 - x3 - x4 = -6
x1 + 2x2 + 3x3 - x4 = -4

"""

mas = [[1, -4, 0, -1],
       [1, 1, 2, 3],
       [2, 3, -1, -1],
       [1, 2, 3, -1]]

h = [2, 1, -6, -4]


# Визначник
def vuzn4x(mas):
    # Визначник 3 порядку (Правило трикутника)
    def minor(mas1):
        return (mas1[0][0] * mas1[1][1] * mas1[2][2] +
                mas1[0][1] * mas1[1][2] * mas1[2][0] +
                mas1[1][0] * mas1[2][1] * mas1[0][2] -
                mas1[0][2] * mas1[1][1] * mas1[2][0] -
                mas1[0][1] * mas1[1][0] * mas1[2][2] -
                mas1[1][2] * mas1[2][1] * mas1[0][0])

    def create_mas1(i1, j1):
        mas1 = [
            [mas[i][j] for j in range(4) if j != j1] for i in range(4) if i != i1
        ]
        return mas1

    # Алгебраїчні доповнення
    def alg(i, j):
        return ((-1) ** (i + j)) * minor(create_mas1(i, j))

    a = 0
    for i in range(4):
        a += mas[0][i] * alg(0, i)

    return a


# Метод Крамера

def create_mas_n(n):
    # Створюємо новий масив і копіюємо дані з оригінального масиву
    mas1 = [row[:] for row in mas]

    # Змінюємо відповідний стовпець у новому масиві за значеннями зі списку
    for i in range(len(mas1)):
        mas1[i][n - 1] = h[i]

    return mas1

print("Метод Крамера:")
for i in range(4):
    print(f"x{i + 1} = ", vuzn4x(create_mas_n(i + 1)) / vuzn4x(mas))


# Жорданові виключення (1 раз)
def J_exeptions(mas, i1, j1):
    a = mas[i1][j1]  # ключовий елемент
    mas1 = copy.deepcopy(mas)  # робить копію масива лише по значенням
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            if j == j1 and i != i1:
                mas[i][j] /= a
                continue
            elif i == i1 and j != j1:
                mas[i][j] = -mas[i][j]
            elif i == i1 and j == j1:
                mas[i1][j1] = 1
            else:
                mas[i][j] = (a * mas1[i][j]) - (mas1[i1][j] * mas1[i][j1])

            mas[i][j] /= a
    return mas


# Метод Жордана-Гауса

def remove_column(mas, col):
    for row in mas:
        del row[col]


def append_element_to_rows(mas, h):
    for i in range(len(mas)):
        mas[i].append(-h[i])

mas_j = copy.deepcopy(mas)
append_element_to_rows(mas_j, h)
i = 3
k = 0
while i >= 0:
    mas_j = J_exeptions(mas_j, k, i)
    remove_column(mas_j, i)
    i -= 1
    k += 1

print("Метод Жордана - Гауса:")
for i in range(4):
    print(f"x{i + 1} = ", mas_j[-(i+1)][0])

# Метод Гауса

mas_g = copy.deepcopy(mas)
append_element_to_rows(mas_g, h)

x = []
i = 3
k = 0
while i >= 0:
    mas_g = J_exeptions(mas_g, 0, i)
    remove_column(mas_g, i)
    x.append(mas_g.pop(0))
    k += 1
    i -= 1

x1 = x[3][0]
x2 = (x[2][0] * x1) + x[2][1]
x3 = (x[1][0] * x1) + (x[1][1] * x2) + x[1][2]
x4 = (x[0][0] * x1) + (x[0][1] * x2) + (x[0][2] * x3) + x[0][3]
print("Метод Гауса:")
print(" x1 = ", x1, "\n", "x2 = ", x2, "\n", "x3 = ", x3, "\n", "x4 = ", x4)

# Метод оберненої матриці
mas_o = copy.deepcopy(mas)
for i in range(len(mas_o[0])):
    mas_o = J_exeptions(mas_o, i, i)

print("Метод оберненої матриці:")
for i in range(4):
    print(f"x{i+1} = ", mas_o[i][0] * h[0] + mas_o[i][1] * h[1] + mas_o[i][2] * h[2] + mas_o[i][3] * h[3])

