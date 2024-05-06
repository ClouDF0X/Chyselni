"""

y' = 3x^2 + 0.1 * x * y

y(0) = 0.2

[0, 1]

h = 0.1
"""


def f(x, y):
    return (3 * x**2) + (0.1 * x * y)

a = 0
b = 1
h = 0.1
y0 = 0.2


def eilera(a, b, h, y0, f):
    n = int((b - a)/h)
    yk = y0
    for i in range(0, n):
        y = yk + h * f(a, yk)
        print(f"f(x{i+1}) = ", y)
        a += h  # x
        yk = y

print("Метод Ейлера")
eilera(a, b, h, y0, f)
print("--"*10)


def rynge_kyta(a, b, h, y0, f):
    n = int((b - a) / h)
    yk = y0
    for i in range(0, n):
        k1 = f(a, yk)
        k2 = f(a + h/2, yk + (h*k1)/2)
        k3 = f(a + h/2, yk + (h*k2)/2)
        k4 = f(a + h/2, yk + (h*k3)/2)
        y = yk + (1/6 * ((k1 + (2 * k2) + (2 * k3) + k4) * h))
        print(f"f(x{i+1}) = ", y)
        a += h  # x
        yk = y

print("Метод Рунге - Кутта")
rynge_kyta(a, b, h, y0, f)
print("--"*10)


def adamsa(a, b, h, y0, f):
    n = int((b - a) / h)
    yk = y0
    fi = []
    for i in range(0, 4):
        k1 = f(a, yk)
        fi.append(k1)
        k2 = f(a + h / 2, yk + (h * k1) / 2)
        k3 = f(a + h / 2, yk + (h * k2) / 2)
        k4 = f(a + h / 2, yk + (h * k3) / 2)
        y = yk + (1 / 6 * ((k1 + (2 * k2) + (2 * k3) + k4) * h))
        print(f"f(x{i + 1}) = ", y)
        a += h  # x
        yk = y
    for i in range(4, n):
        y = yk + (h/24) * ((fi[-1] * 55) - (59 * fi[-2]) + (37 * fi[-3]) - (9 * fi[-4]))
        # print(f"TEST:f(x{i + 1}) = ", y)
        fn = f(a, y)
        y = yk + (h/24) * ((9 * fn) + (19 * fi[-1]) - (5 * fi[-2]) + fi[-3])
        fi.append(f(a, y))
        print(f"f(x{i + 1}) = ", y)
        a += h
        yk = y

print("Метод Адамса")
adamsa(a, b, h, y0, f)
print("--"*10)


def milna(a, b, h, y0, f):
    n = int((b - a) / h)
    yk = y0
    fi = []
    yi = []
    for i in range(0, 4):
        k1 = f(a, yk)
        fi.append(k1)
        k2 = f(a + h / 2, yk + (h * k1) / 2)
        k3 = f(a + h / 2, yk + (h * k2) / 2)
        k4 = f(a + h / 2, yk + (h * k3) / 2)
        y = yk + (1 / 6 * ((k1 + (2 * k2) + (2 * k3) + k4) * h))
        yi.append(y)
        print(f"f(x{i + 1}) = ", y)
        a += h  # x
        yk = y
    for i in range(4, n):
        y = yi[0] + ((4/3) * h) * (2 * fi[-1] - fi[-2] + (2 * fi[-3]))
        fn = f(a, y)
        y = yi[-2] + (h/3) * (fi[-2] + (4 * fi[-1]) + fn)
        fi.append(f(a, y))
        print(f"f(x{i + 1}) = ", y)
        a += h  # x
        yi.append(y)

print("Метод Мілна")
milna(a, b, h, y0, f)
print("--"*10)
