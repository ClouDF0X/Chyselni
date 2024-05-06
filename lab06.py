import math
import random
"""

Варіант 17

1)
a = 0.6
b = 1.6

f(x) = 1 / (sqrt(x^2 + 0.8))
Має бути: 0.7164

2)
a = 0.6
b = 1.4

f(x) = x^2 * cos(x)
Має бути: 0.3721
"""
a1 = 0.6
b1 = 1.6


def f1(x):
    return 1 / (math.sqrt(x**2 + 0.8))


a2 = 0.6
b2 = 1.4


def f2(x):
    return x**2 * math.cos(x)


def rectangle_method(a, b, f, c, n=1000):
    h = (b - a)/n
    y = 0
    if c == "l":
        for i in range(0, n):
            y += f(a + i * h)
    elif c == "r":
        for i in range(1, n + 1):
            y += f(a + i * h)
    else:
        for i in range(0, n):
            y += f(a + (i + 0.5) * h)
    return h * y


print("Ліві")
print(rectangle_method(a1, b1, f1, "l"))
print(rectangle_method(a2, b2, f2, "l"))

print("Праві")
print(rectangle_method(a1, b1, f1, "r"))
print(rectangle_method(a2, b2, f2, "r"))

print("Середні")
print(rectangle_method(a1, b1, f1, "с"))
print(rectangle_method(a2, b2, f2, "с"))


def trapezoid_method(a, b, f, n=1000):
    h = (b - a) / n
    y = (f(a)+f(b))/2
    for i in range(1, n):
        y += f(a + i * h)
    return y * h

print("Трапеція")
print(trapezoid_method(a1, b1, f1))
print(trapezoid_method(a2, b2, f2))


def simpson_method(a, b, f, n=1000):
    h = (b - a) / n
    y = f(a) + f(b)
    m = int(n/2)
    c1 = 0
    for i in range(1, m + 1):
        c1 += f(a + (2 * i - 1) * h)
    c1 *= 4
    c2 = 0
    for i in range(0, m):
        c2 += f(a + (2 * i) * h)
    c2 *= 2
    y = y + c1 + c2
    return y * (h/3)

print("Сімсон")
print(simpson_method(a1, b1, f1))
print(simpson_method(a2, b2, f2))


def montecarlo_method(a, b, f, n=1000):
    h = (b - a) / n
    max_y = f(a)
    for i in range(1, n):
        max_y = max(max_y, f(a + i * h))
    x1 = (b-a)
    s = max_y * x1
    n1 = 0
    for i in range(0, n):
        x = random.uniform(a, b)
        y = random.uniform(0, max_y)
        if y <= f(x):
            n1 += 1
    return (s * n1) / n

print("Монте - Карло")
print(montecarlo_method(a1, b1, f1))
print(montecarlo_method(a2, b2, f2))


def doble_counting(a, b, f, n, eps=0.001):
    a1 = 0
    while a > eps:
        a1 = trapezoid_method(a, b, f, n)
        n *= 2
        a2 = trapezoid_method(a, b, f, n)
        a = abs(a1 - a2)

    return a1

print("Повторне")
print(doble_counting(a1, b1, f1, 10))
print(doble_counting(a2, b2, f2, 10))
