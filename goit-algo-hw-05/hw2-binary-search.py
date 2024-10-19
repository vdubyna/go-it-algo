def binary_search_with_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])  # Знайдено точний збіг

        if arr[mid] < target:
            left = mid + 1  # Продовжуємо пошук у правій частині
        else:
            upper_bound = arr[mid]
            right = mid - 1  # Продовжуємо пошук у лівій частині

    # Якщо елемент не знайдено, повертаємо найближчу верхню межу
    return (iterations, upper_bound)


# Тестуємо функцію
arr = [0.5, 1.2, 2.4, 3.5, 4.8, 6.9, 8.1]
target = 3.0

result = binary_search_with_upper_bound(arr, target)
print(result)  # Очікуваний результат: (кількість ітерацій, 3.5)