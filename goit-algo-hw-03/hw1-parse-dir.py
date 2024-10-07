import os
import shutil
import argparse

def copy_and_sort_files(src_dir, dest_dir):
    """
    Рекурсивно копіює файли з вихідної директорії в директорію призначення.
    Файли сортуються в підпапки відповідно до розширення файлу.
    """
    try:
        # Перебираємо всі елементи в вихідній директорії
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            # Якщо елемент - директорія, викликаємо функцію рекурсивно
            if os.path.isdir(item_path):
                new_dest_dir = os.path.join(dest_dir, item)
                os.makedirs(new_dest_dir, exist_ok=True)  # Створюємо папку в директорії призначення
                copy_and_sort_files(item_path, new_dest_dir)
            else:
                # Якщо елемент - файл, обробляємо його
                file_name, file_extension = os.path.splitext(item)  # Отримуємо ім'я файлу та розширення
                file_ext = file_extension.lstrip('.').lower()       # Видаляємо крапку спереду та переводимо в нижній регістр
                if file_ext:  # Перевіряємо, що розширення не порожнє
                    ext_dir = os.path.join(dest_dir, file_ext)
                    os.makedirs(ext_dir, exist_ok=True)  # Створюємо папку для розширення, якщо вона не існує
                    shutil.copy2(item_path, ext_dir)  # Копіюємо файл у відповідну папку
    except Exception as e:
        print(f"Помилка при обробці '{src_dir}': {e}")

def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів.")
    parser.add_argument("src", help="Вихідна директорія")
    parser.add_argument("dest", nargs='?', default="dist", help="Директорія призначення (за замовчуванням: dist)")
    args = parser.parse_args()

    # Перевіряємо наявність вихідної директорії
    if not os.path.exists(args.src):
        print(f"Вихідна директорія '{args.src}' не існує!")
        return

    # Створюємо директорію призначення, якщо вона не існує
    os.makedirs(args.dest, exist_ok=True)

    # Виконуємо рекурсивне копіювання та сортування
    copy_and_sort_files(args.src, args.dest)
    print(f"Файли успішно скопійовані та відсортовані в '{args.dest}'")

if __name__ == "__main__":
    main()