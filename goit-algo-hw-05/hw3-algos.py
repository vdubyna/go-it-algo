import timeit

# Реалізація алгоритму Боєра-Мура
def boyer_moore_search(text, pattern):
    m, n = len(pattern), len(text)
    if m > n:
        return -1

    # Таблиця зміщень
    shift = {char: m for char in set(text)}
    for i in range(m - 1):
        shift[pattern[i]] = m - 1 - i

    i = m - 1
    while i < n:
        j = m - 1
        while j >= 0 and text[i] == pattern[j]:
            i -= 1
            j -= 1
        if j < 0:
            return i + 1
        i += shift.get(text[i], m)
    return -1

# Реалізація алгоритму Кнута-Морріса-Пратта (KMP)
def kmp_search(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return 0

    lps = [0] * m
    j = 0  # індекс підрядка

    # Обчислення LPS масиву
    compute_lps(pattern, m, lps)

    i = 0  # індекс тексту
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def compute_lps(pattern, m, lps):
    length = 0  # довжина попереднього LPS
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

# Реалізація алгоритму Рабіна-Карпа
def rabin_karp_search(text, pattern, prime=101):
    m, n = len(pattern), len(text)
    d = 256  # розмір алфавіту
    p = 0  # значення хеша підрядка
    t = 0  # значення хеша тексту
    h = 1

    # Значення h = d^(m-1) % prime
    for i in range(m - 1):
        h = (h * d) % prime

    # Обчислення початкового хеша підрядка та тексту
    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    # Пошук у тексті
    for i in range(n - m + 1):
        if p == t:  # Якщо значення хешів збігаються
            if text[i:i + m] == pattern:
                return i

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t < 0:
                t += prime

    return -1

# Тестові функції для вимірювання часу виконання
def measure_execution_time(text, pattern):
    algorithms = {
        "Boyer-Moore": boyer_moore_search,
        "KMP": kmp_search,
        "Rabin-Karp": rabin_karp_search
    }
    results = {}
    for name, algorithm in algorithms.items():
        time_taken = timeit.timeit(lambda: algorithm(text, pattern), number=1000)
        results[name] = time_taken
    return results

def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Тестовий пошук

text1 = load_text_from_file('data/стаття 1.txt')
text2 = load_text_from_file('data/стаття 2.txt')
pattern_existing = "алгоритм"
pattern_non_existing = "вигаданийпідрядок"

# Вимірювання часу виконання для кожного алгоритму на статті 1
results_text1_existing = measure_execution_time(text1, pattern_existing)
results_text1_non_existing = measure_execution_time(text1, pattern_non_existing)

# Вимірювання часу виконання для кожного алгоритму на статті 2
results_text2_existing = measure_execution_time(text2, pattern_existing)
results_text2_non_existing = measure_execution_time(text2, pattern_non_existing)

# Підсумкові результати
print("Час виконання для статті 1 (існуючий підрядок):", results_text1_existing)
print("Час виконання для статті 1 (вигаданий підрядок):", results_text1_non_existing)
print("Час виконання для статті 2 (існуючий підрядок):", results_text2_existing)
print("Час виконання для статті 2 (вигаданий підрядок):", results_text2_non_existing)