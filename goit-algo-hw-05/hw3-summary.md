# Порівняння ефективності алгоритмів пошуку підрядка

## Вступ
Було проведено тестування трьох алгоритмів пошуку підрядка (Боєр-Мур, Кнута-Морріса-Пратта, Рабіна-Карпа) для двох текстових файлів та двох видів підрядків: існуючого та вигаданого. Наведені результати демонструють ефективність кожного алгоритму в різних умовах.

## Результати

| Алгоритм        | Стаття 1 (існ.) | Стаття 1 (виг.) | Стаття 2 (існ.) | Стаття 2 (виг.) |
|-----------------|----------------|----------------|----------------|----------------|
| Боєр-Мур        | 0.396 с        | 0.508 с        | 0.586 с        | 0.722 с        |
| Кнута-Морріса-Пратта | 0.026 с    | 1.559 с        | 0.378 с        | 2.252 с        |
| Рабін-Карп      | 0.035 с        | 2.057 с        | 0.486 с        | 2.916 с        |

## Висновки
- **Кнута-Морріса-Пратта (KMP)** показав найкращі результати для пошуку існуючих підрядків у тексті.
- **Боєр-Мур** виявився найшвидшим для пошуку вигаданих підрядків у тексті.
- **Рабін-Карп** був менш ефективним порівняно з іншими алгоритмами в усіх тестах.

Алгоритм Боєра-Мура найбільш ефективний для пошуку вигаданих підрядків, оскільки його оптимізація націлена на зменшення кількості перевірок і максимізацію стрибків у випадках невідповідності, що дозволяє швидко обробляти текст.