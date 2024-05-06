import sympy as sp

# Створення символьної змінної
t = sp.symbols('t')

# # Визначення функції
# f = x**2 - 2 * sp.cos(x)
#
# # Обчислення похідної
# derivative = sp.diff(f, x)

# # Виведення результату
# print("Функція:", f)
# print("Похідна:", derivative)

xi = [1.340, 1.345, 1.350, 1.355, 1.360, 1.365, 1.370, 1.375, 1.380, 1.385, 1.390, 1.395]
x = 1.3463
h = xi[1] - xi[0]
t1 = (x - xi[0])/h
p = t
for i in range(2):
    p = sp.expand(p * (t - (i + 1)))
    print(p)
p = sp.diff(p, t)
print(p)
p = p.subs(t, t1)
print(p)