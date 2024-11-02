items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортування за співвідношенням калорій до вартості у порядку спадання
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []

    for name, item in sorted_items:
        if item['cost'] <= budget:
            selected_items.append(name)
            total_calories += item['calories']
            budget -= item['cost']

    return selected_items, total_calories

def dynamic_programming(items, budget):
    # Список вартостей та калорій
    costs = [item['cost'] for item in items.values()]
    calories = [item['calories'] for item in items.values()]
    names = list(items.keys())

    # Таблиця для динамічного програмування
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнення таблиці
    for i in range(1, n + 1):
        for b in range(budget + 1):
            if costs[i - 1] <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][b] = dp[i - 1][b]

    # Відновлення вибраних предметів
    total_calories = dp[n][budget]
    selected_items = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            selected_items.append(names[i - 1])
            b -= costs[i - 1]

    return selected_items, total_calories

# Приклад використання:
budget = 100

# Жадібний алгоритм
greedy_selected, greedy_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_selected)
print("Сумарна калорійність:", greedy_calories)

# Алгоритм динамічного програмування
dp_selected, dp_calories = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print("Вибрані страви:", dp_selected)
print("Сумарна калорійність:", dp_calories)