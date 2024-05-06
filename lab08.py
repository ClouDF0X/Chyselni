import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Обмеження (ліві частини нерівностей)
A = np.array([[2, 7], [2, -6], [1, 2], [-1, -2]])
# Праві частини нерівностей
b = np.array([2, 2, 1, -1])
# Коефіцієнти функції z = 4x1 + x2 + 10
c = np.array([-4, -1])

# Знаходимо многокутник розв'язків
res = linprog(c, A_ub=A, b_ub=b)
x1, x2 = res.x

# Виводимо результати
print(f"Максимальне значення функції z: {res.fun:.2f}")
print(f"Розв'язок: x1 = {x1:.2f}, x2 = {x2:.2f}")

# Побудова графіку
x1_vals = np.linspace(0, 1.5, 100)
x2_vals1 = (2 - 2 * x1_vals) / 7
x2_vals2 = (2 - 2 * x1_vals) / 6
x2_vals3 = (1 - x1_vals) / 2
x2_vals4 = (1 - x1_vals) / 2

plt.figure(figsize=(8, 6))
plt.plot(x1_vals, x2_vals1, label=r"$2x_1 + 7x_2 \geq 2$")
plt.plot(x1_vals, x2_vals2, label=r"$2x_1 - 6x_2 \leq 2$")
plt.plot(x1_vals, x2_vals3, label=r"$x_1 + 2x_2 \leq 1$")
plt.plot(x1_vals, x2_vals4, label=r"$x_1 + 2x_2 \geq 1$")

plt.fill_between(x1_vals, x2_vals1, x2_vals2, color="gray", alpha=0.3)

plt.scatter(x1, x2, color="red", marker="o", label="Розв'язок")
plt.xlabel("$x_1$")
plt.ylabel("$x_2$")
plt.title("Многокутник розв'язків")
plt.grid(True)
plt.legend()
plt.show()
