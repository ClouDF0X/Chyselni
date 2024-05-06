# Варіант 17

"""
Система

1,7x1 - 2,2x2 + 3,0x3 = 1,8
2,1x1 + 1,9x2 - 2,3x3 = 2,8
4,2x1 + 3,9x2 - 3,1x3 = 5,1

5,9x1 + 1,7x2 - 0,1x3 = 6,9
1,7x1 - 2,4x2 = 2,8
-0,1x2 - 1,5x3 = 0,5

"""
# Введення коефіцієнтів системи рівнянь
A = [[1.7, -2.2, 3.0],
     [2.1, 1.9, -2.3],
     [4.2, 3.9, -3.1]]

h = [1.8, 2.8, 5.1]

A2 = [[5.9, 1.7, -0.1],
      [1.7, -2.4, 0],
      [-0.1, 0, -1.5]]

h2 = [6.9, 2.8, 0.5]



# TEST
# перевірка достатніх умов
# def verification_decent_condition(mas):
#     res = True
#     # рядок
#     for i in range(len(mas[0])):
#         if (abs(mas[i][0])+abs(mas[i][1])+abs(mas[i][2])) > 1:
#             res = False
#             break
#
#     # стовпчик
#     if not res:
#         res = True
#         for j in range(len(mas)):
#             if (abs(mas[0][j]) + abs(mas[1][j]) + abs(mas[2][j])) > 1:
#                 res = False
#                 break
#     return res
#
#
# # перевірка діагоналі
def verification_diagonal(mas):
    res = True
    for i in range(len(mas)):
        sum = 0
        for j in range(len(mas[i])):
            if j == i:
                continue
            sum += abs(mas[i][j])
        if abs(mas[i][i]) < sum:
            res = False
            break

    return res
#
#
# def compute_B(A):
#     num_rows, num_cols = len(A), len(A[0])
#     B = [[0] * num_cols for _ in range(num_rows)]
#
#     for i in range(num_rows):
#         for j in range(num_cols):
#             if i != j:
#                 B[i][j] = -A[i][j] / A[i][i]
#
#     return B
#
#
# def matrix_multiplication(A, v):
#     num_rows_A, num_cols_A = len(A), len(A[0])
#     if num_cols_A != len(v):
#         raise ValueError("Кількість стовпчиків матриці A повинна дорівнювати довжині вектора v.")
#
#     # Створюємо пустий вектор для результату
#     result = [0] * num_rows_A
#
#     # Перемноження матриці на вектор
#     for i in range(num_rows_A):
#         for j in range(num_cols_A):
#             result[i] += A[i][j] * v[j]
#
#     return result
#
# def vector_addition(v1, v2):
#     if len(v1) != len(v2):
#         raise ValueError("Вектори мають різну довжину і не можуть бути додані.")
#
#     result = [0] * len(v1)
#     for i in range(len(v1)):
#         result[i] = v1[i] + v2[i]
#
#     return result
#
# def compute_shift_vector(A, b):
#     n = len(b)
#     c = [0] * n
#
#     for i in range(n):
#         c[i] = b[i] / A[i][i]
#
#     return c
#
#
# def iteration_linear_system(A, b, initial_guess, epsilon=0.001, max_iterations=1000):
#     n = len(b)
#     x = initial_guess
#     iterations = 0
#
#     B = compute_B(A)
#     c = compute_shift_vector(A, b)
#
#     while True:
#         x_next = matrix_multiplication(B, x)
#         x_next = vector_addition(x_next, c)
#
#         iterations += 1
#         # print(x)
#         # print(x_next)
#         # print(max(abs(x_next[i] - x[i]) for i in range(n)))
#         if max(abs(x_next[i] - x[i]) for i in range(n)) < epsilon or iterations >= max_iterations:
#             break
#
#         x = x_next
#
#     return x_next, iterations
#
# print(iteration_linear_system(A, h, x0))


# Метод простої ітерації
def itteration(A, h, eps=0.001):
    x1, x2, x3 = h[0], h[1], h[2]
    a = 0
    while True:
        a += 1
        x1_new = (-(A[0][1]/A[0][0]) * x2) + (-(A[0][2]/A[0][0]) * x3) + (h[0]/A[0][0])
        x2_new = (-(A[1][0] / A[1][1]) * x1) + (-(A[1][2] / A[1][1]) * x3) + (h[1] / A[1][1])
        x3_new = (-(A[2][0] / A[2][2]) * x1) + (-(A[2][1] / A[2][2]) * x2) + (h[2] / A[2][2])
        # if (abs(max(x1_new, x2_new, x3_new) - max(x1, x2, x3))) < eps:
        if abs(x1 - x1_new)<eps and abs(x2 - x2_new)<eps and abs(x3 - x3_new) < eps:
            break
        x1, x2, x3 = x1_new, x2_new, x3_new
    return x1, x2, x3, a
print(verification_diagonal(A2))
print(itteration(A2, h2))
# Метод Зейделя

def zaidela(A, h, eps=0.001):
    x1, x2, x3 = h[0], h[1], h[2]
    a = 0
    while True:
        a += 1
        tx1, tx2, tx3 = x1, x2, x3
        x1 = (-(A[0][1]/A[0][0]) * x2) + (-(A[0][2]/A[0][0]) * x3) + (h[0]/A[0][0])
        x2 = (-(A[1][0] / A[1][1]) * x1) + (-(A[1][2] / A[1][1]) * x3) + (h[1] / A[1][1])
        x3 = (-(A[2][0] / A[2][2]) * x1) + (-(A[2][1] / A[2][2]) * x2) + (h[2] / A[2][2])
        if abs(x1 - tx1)<eps and abs(x2 - tx2)<eps and abs(x3 - tx3) < eps:
            break

    return x1, x2, x3, a

print(zaidela(A2, h2))
