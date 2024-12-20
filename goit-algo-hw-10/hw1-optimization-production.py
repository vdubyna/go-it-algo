import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Визначення змінних
x1 = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  # Кількість Лимонаду
x2 = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')  # Кількість Фруктового соку

# Функція цілі (Максимізація загальної кількості продуктів)
model += x1 + x2, "Total_Production"

# Обмеження на ресурси

# 1. Обмеження на воду
# Вода використовується для виробництва "Лимонаду" (2 одиниці води на одиницю лимонаду)
# та "Фруктового соку" (1 одиниця води на одиницю фруктового соку).
# Максимум 100 одиниць води доступно.
model += 2 * x1 + x2 <= 100, "Water_Limit"

# 2. Обмеження на цукор
# Цукор використовується тільки для виробництва "Лимонаду" (1 одиниця цукру на одиницю лимонаду).
# Максимум 50 одиниць цукру доступно.
model += x1 <= 50, "Sugar_Limit"

# 3. Обмеження на лимонний сік
# Лимонний сік використовується тільки для виробництва "Лимонаду" (1 одиниця лимонного соку на одиницю лимонаду).
# Максимум 30 одиниць лимонного соку доступно.
model += x1 <= 30, "Lemon_Juice_Limit"

# 4. Обмеження на фруктове пюре
# Фруктове пюре використовується для виробництва "Фруктового соку" (2 одиниці пюре на одиницю фруктового соку).
# Максимум 40 одиниць фруктового пюре доступно.
model += 2 * x2 <= 40, "Fruit_Puree_Limit"

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Кількість Лимонаду:", x1.varValue)
print("Кількість Фруктового соку:", x2.varValue)
print("Загальна кількість продуктів:", pulp.value(model.objective))