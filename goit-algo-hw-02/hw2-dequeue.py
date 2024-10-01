from collections import deque
import string

def preprocess_string(input_string):
    """Перетворює рядок у нижній регістр та видаляє небуквені символи."""
    # Крок 1: Перетворюємо рядок на малі літери
    lower_case_string = input_string.lower()

    # Крок 2: Вибираємо тільки букви (ігноруючи все інше)
    filtered_chars = []
    for char in lower_case_string:
        if char in string.ascii_letters:  # Перевіряємо, чи є символ літерою
            filtered_chars.append(char)   # Додаємо його до списку

    # Крок 3: Об'єднуємо всі літери у суцільний рядок
    filtered_string = ''.join(filtered_chars)

    return filtered_string

def is_palindrome(input_string):
    """Перевіряє, чи є рядок паліндромом."""
    # Створюємо двосторонню чергу (deque)
    char_deque = deque(preprocess_string(input_string))

    # Порівнюємо символи з початку та кінця deque, поки він не стане порожнім або не знайдемо невідповідність
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False  # Символи не збігаються, не є паліндромом

    return True  # Усі символи збігаються, рядок є паліндромом

# Приклади використання
test_strings = [
    "A man, a plan, a canal: Panama",
    "racecar",
    "No lemon, no melon",
    "Hello, world!",
    "Was it a car or a cat I saw"
]

for s in test_strings:
    print(f"'{s}' is a palindrome: {is_palindrome(s)}")