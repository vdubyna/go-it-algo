# Оптимальна стратегія: щоб мінімізувати загальні витрати на з’єднання кабелів,
# потрібно кожного разу з’єднувати два найкоротші кабелі, що є.
# Таким чином ми використовуємо найменші можливі довжини на кожному етапі об’єднання,
# що призводить до мінімізації сумарних витрат.

import heapq

def min_cost_to_connect_cables(cable_lengths):
    heapq.heapify(cable_lengths)
    total_cost = 0
    while len(cable_lengths) > 1:
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        cost = first + second
        heapq.heappush(cable_lengths, cost)
        total_cost += cost
    return total_cost

# Приклад використання:
cables = [5, 4, 7, 2, 6, 8]
print("Загальні витрати на з'єднання:", min_cost_to_connect_cables(cables))