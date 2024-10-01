def check_brackets(expression):
    """Перевіряє симетрію дужок у виразі."""
    # Створюємо стек для зберігання відкривальних дужок
    stack = []

    # Визначення пар відкривальних і закривальних дужок
    matching_brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # Перебираємо кожен символ у рядку
    for char in expression:
        # Якщо символ є відкривальною дужкою, додаємо його в стек
        if char in matching_brackets.values():  # '(', '{', '['
            stack.append(char)
        # Якщо символ є закривальною дужкою, перевіряємо відповідність
        elif char in matching_brackets:  # ')', '}', ']'
            # Якщо стек порожній або дужки не відповідають, вираз несиметричний
            if not stack or stack.pop() != matching_brackets[char]:
                return "Несиметрично"

    # Якщо стек порожній, усі дужки симетричні
    return "Симетрично" if not stack else "Несиметрично"

# Приклади перевірки
test_expressions = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }",
    "((()))",     # Симетрично
    "{ [ ( ) ] }", # Симетрично
    "{ [ ( ] ) }", # Несиметрично
    "{ [ ) ] }",   # Несиметрично
]

# Перевірка виразів
for expr in test_expressions:
    print(f"'{expr}': {check_brackets(expr)}")