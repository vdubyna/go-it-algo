import random
import timeit
import pandas as pd

# Ваш варіант сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Переміщення елементів масиву, які більше за ключ, на одну позицію вперед
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Timsort: використовується вбудована функція sorted
def timsort(arr):
    return sorted(arr)

# Функція для генерації тестових даних
def generate_data(size, data_type):
    if data_type == "random":
        return [random.randint(0, size) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(size))
    elif data_type == "reversed":
        return list(range(size, 0, -1))

# Параметри тестування
sizes = [100, 1000, 5000, 10000]  # Різні розміри масивів
data_types = ["random", "sorted", "reversed"]  # Типи масивів

# Заміри часу для різних алгоритмів
results = []

for size in sizes:
    for data_type in data_types:
        data = generate_data(size, data_type)

        # Використання timeit для заміру часу
        merge_time = timeit.timeit(lambda: merge_sort(data.copy()), number=10)
        insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=10)
        timsort_time = timeit.timeit(lambda: timsort(data.copy()), number=10)

        # Обчислення відсоткової різниці
        merge_vs_timsort = ((merge_time - timsort_time) / timsort_time) * 100
        insertion_vs_timsort = ((insertion_time - timsort_time) / timsort_time) * 100

        # Додавання результатів у таблицю
        results.append([
            size, data_type, merge_time, insertion_time, timsort_time,
            f"{merge_vs_timsort:.2f}%", f"{insertion_vs_timsort:.2f}%"
        ])

        print(f"Розмір: {size}, Тип даних: {data_type}")
        print(f"  Сортування злиттям: {merge_time:.6f} сек ({merge_vs_timsort:.2f}% відносно Timsort)")
        print(f"  Сортування вставками: {insertion_time:.6f} сек ({insertion_vs_timsort:.2f}% відносно Timsort)")
        print(f"  Timsort: {timsort_time:.6f} сек")
        print("-" * 40)

# Виведення результатів у таблиці для зручності перегляду
df = pd.DataFrame(
    results,
    columns=[
        "Size", "Data Type", "Merge Sort (s)", "Insertion Sort (s)", "Timsort (s)",
        "Merge vs Timsort (%)", "Insertion vs Timsort (%)"
    ]
)

print(df)