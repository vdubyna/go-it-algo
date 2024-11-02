import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_rolls):
    # Ініціалізація лічильника для кожної можливої суми
    sums_count = {i: 0 for i in range(2, 13)}

    # Виконання симуляції
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll_sum = dice1 + dice2
        sums_count[roll_sum] += 1

    # Обчислення ймовірностей
    probabilities = {s: count / num_rolls for s, count in sums_count.items()}
    return probabilities

# Кількість кидків для симуляції
num_rolls = 100000
simulated_probabilities = monte_carlo_simulation(num_rolls)

# Аналітичні ймовірності
analytical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

# Підготовка даних для графіку
sums = list(range(2, 13))
simulated_values = [simulated_probabilities[s] * 100 for s in sums]
analytical_values = [analytical_probabilities[s] * 100 for s in sums]

# Побудова графіку
plt.figure(figsize=(10, 6))
plt.plot(sums, simulated_values, marker='o', label='Монте-Карло')
plt.plot(sums, analytical_values, marker='x', linestyle='--', color='red', label='Аналітичні')
plt.xlabel("Сума на двох кубиках")
plt.ylabel("Ймовірність (%)")
plt.title("Ймовірності сум при киданні двох кубиків: Монте-Карло vs Аналітичні")
plt.legend()
plt.grid(True)
plt.show()

# Вивід ймовірностей для порівняння
print("Результати симуляції методом Монте-Карло:")
for s in sums:
    print(f"Сума {s}: {simulated_probabilities[s]*100:.2f}% (Монте-Карло), {analytical_probabilities[s]*100:.2f}% (Аналітична)")