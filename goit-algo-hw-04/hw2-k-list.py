def merge_two_lists(list1, list2):
    """Функція для злиття двох відсортованих списків."""
    merged = []
    i = j = 0

    # Злийте два списки, порівнюючи кожен елемент
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Додаємо залишкові елементи
    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged

def merge_k_lists(lists):
    """Функція для злиття k відсортованих списків у один."""
    if not lists:
        return []

    # Послідовно зливаємо списки два за раз
    while len(lists) > 1:
        merged_lists = []

        # Об'єднуємо сусідні списки два за раз
        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i + 1] if i + 1 < len(lists) else []
            merged_lists.append(merge_two_lists(list1, list2))

        # Оновлюємо наш список із залишковими об'єднаними списками
        lists = merged_lists

    return lists[0]

# Тестування функції
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)