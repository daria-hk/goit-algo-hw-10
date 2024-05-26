import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Функція для перевірки точок всередині сірої зони
def is_inside(a, b, x, y):
    return a <= x <= b and 0 <= y <= f(x)

# Генерація випадкових точок
points = [(random.uniform(a, b), random.uniform(0, f(b))) for _ in range(15000)]

# Відбір точок, що знаходяться всередині сірої зони:
inside_points = [point for point in points if is_inside(a, b, point[0], point[1])]

# Кількість усіх точок та точок всередині
N = len(points)
M = len(inside_points)

# Обчислення інтеграла
grey_area= (b - a) * f(b)
integral= grey_area * M / N
result, error = spi.quad(f, a, b)

# Виведення результатів
print(f"Кількість точок всередині сірої зони: {M}, загальна кількість точок: {N}")
print(f"Значення інтеграла функції за методом Монте-Карло: {integral}, та значення інтеграла за звичайним обчисленням {result}")

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Малювання випадкових точок
points_x, points_y = zip(*points)
ax.scatter(points_x, points_y, color='blue', s=1, alpha=0.5, label='Випадкові точки')

# Малювання точок всередині сірої зони
inside_x, inside_y = zip(*inside_points)
ax.scatter(inside_x, inside_y, color='green', s=1, alpha=0.5, label='Точки під кривою')

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
