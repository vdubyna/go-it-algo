import matplotlib.pyplot as plt
import numpy as np

def draw_branch(ax, x, y, angle, length, level):
    """Малює гілку дерева Піфагора."""
    if level == 0:
        return

    # Обчислення кінцевих координат гілки
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    # Малюємо гілку
    ax.plot([x, x_end], [y, y_end], color="green", lw=2)

    # Зменшуємо довжину для наступних гілок
    new_length = length * 0.7

    # Малюємо ліву і праву гілки під кутом 45 градусів
    draw_branch(ax, x_end, y_end, angle + np.pi / 4, new_length, level - 1)
    draw_branch(ax, x_end, y_end, angle - np.pi / 4, new_length, level - 1)

def main():
    # Введення рівня рекурсії від користувача
    level = int(input("Введіть рівень рекурсії для дерева Піфагора: "))

    # Налаштування графіку
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_axis_off()

    # Початкові параметри для стовбура дерева
    x, y = 0, 0  # Початкова точка
    length = 100  # Довжина першої гілки
    angle = np.pi / 2  # Початковий кут (вертикальний)

    # Малювання дерева
    draw_branch(ax, x, y, angle, length, level)
    plt.show()

# Запуск основної функції
main()