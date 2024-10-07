def hanoi_tower(n, source, target, auxiliary, state):
    """
    Рекурсивна функція для переміщення дисків у задачі Ханойських веж.

    :param n: Кількість дисків
    :param source: Початковий стрижень (наприклад, 'A')
    :param target: Стрижень, на який потрібно перемістити всі диски (наприклад, 'C')
    :param auxiliary: Допоміжний стрижень (наприклад, 'B')
    :param state: Поточний стан стрижнів (словник, який відслідковує розташування дисків)
    """
    if n == 1:
        # Переміщення одного диска з джерела на цільовий стрижень
        print(f"Перемістити диск з {source} на {target}: {state[source][-1]}")
        # Перемістити диск
        state[target].append(state[source].pop())
        print(f"Проміжний стан: {state}")
    else:
        # Перемістити n-1 дисків з джерела на допоміжний стрижень
        hanoi_tower(n - 1, source, auxiliary, target, state)

        # Перемістити залишковий n-й диск з джерела на цільовий стрижень
        print(f"Перемістити диск з {source} на {target}: {state[source][-1]}")
        state[target].append(state[source].pop())
        print(f"Проміжний стан: {state}")

        # Перемістити n-1 дисків з допоміжного стрижня на цільовий стрижень
        hanoi_tower(n - 1, auxiliary, target, source, state)

def main():
    # Введення користувачем кількості дисків
    try:
        n = int(input("Введіть кількість дисків (n >= 1): "))
        if n < 1:
            print("Кількість дисків має бути не менше 1.")
            return
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    # Початковий стан стрижнів
    state = {
        'A': list(range(n, 0, -1)),  # Початковий стрижень A містить n дисків
        'B': [],  # Допоміжний стрижень B
        'C': []   # Цільовий стрижень C
    }

    print(f"Початковий стан: {state}")

    # Виклик рекурсивної функції для переміщення дисків з A на C, використовуючи B
    hanoi_tower(n, 'A', 'C', 'B', state)

    print(f"Кінцевий стан: {state}")

if __name__ == "__main__":
    main()