import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа

# Кількість випадкових точок для методу Монте-Карло
N = 100000

# Метод Монте-Карло для обчислення інтеграла
x_random = np.random.uniform(a, b, N)  # Випадкові значення x
y_random = np.random.uniform(0, f(b), N)  # Випадкові значення y

# Кількість точок, що лежать під кривою
points_under_curve = np.sum(y_random < f(x_random))

# Площа прямокутника
rect_area = (b - a) * f(b)

# Оцінка інтеграла методом Монте-Карло
monte_carlo_integral = (points_under_curve / N) * rect_area

# Аналітичне обчислення інтеграла за допомогою функції quad
analytical_integral, error = spi.quad(f, a, b)

# Виведення результатів
print("Метод Монте-Карло: ", monte_carlo_integral)
print("Аналітичне обчислення (quad): ", analytical_integral)
print("Абсолютна помилка: ", abs(monte_carlo_integral - analytical_integral))

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

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