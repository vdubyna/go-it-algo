import turtle

def draw_koch_segment(length, level):
    """
    Малює один сегмент кривої Коха з рекурсивною деталізацією.

    :param length: Довжина відрізка
    :param level: Рівень рекурсії
    """
    if level == 0:
        turtle.forward(length)
    else:
        # Кожен відрізок поділяється на чотири частини, що утворюють "зубчастий" фрактал
        length /= 3.0
        draw_koch_segment(length, level - 1)  # Перша третина
        turtle.left(60)                       # Повертаємо черепашку на 60 градусів ліворуч
        draw_koch_segment(length, level - 1)  # Друга третина
        turtle.right(120)                     # Повертаємо черепашку на 120 градусів праворуч
        draw_koch_segment(length, level - 1)  # Третя третина
        turtle.left(60)                       # Повертаємо черепашку на 60 градусів ліворуч
        draw_koch_segment(length, level - 1)  # Четверта третина

def draw_snowflake(length, level):
    """
    Малює повну сніжинку Коха, складається з трьох сегментів.

    :param length: Довжина сторони сніжинки
    :param level: Рівень рекурсії
    """
    for _ in range(3):
        draw_koch_segment(length, level)  # Малюємо сегмент
        turtle.right(120)                 # Повертаємо на 120 градусів праворуч для переходу до наступної сторони

def main():
    # Налаштування екрану
    turtle.setup(800, 600)
    turtle.speed(0)  # Максимальна швидкість малювання
    turtle.penup()
    turtle.goto(-300, 100)  # Початкова позиція
    turtle.pendown()

    # Запит рівня рекурсії у користувача
    try:
        level = int(input("Введіть рівень рекурсії (рекомендується 3-4): "))
    except ValueError:
        print("Введіть коректне ціле число для рівня рекурсії.")
        return

    # Малюємо сніжинку Коха
    draw_snowflake(300, level)

    # Завершення та показ результату
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()