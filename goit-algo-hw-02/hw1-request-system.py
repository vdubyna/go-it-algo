import queue
import random
import time

class RequestSystem:
    def __init__(self):
        """Ініціалізація системи: створення черги та лічильника заявок."""
        self.request_queue = queue.Queue()
        self.request_id_counter = 0

    def generate_request(self):
        """Генерує нову заявку та додає її до черги."""
        self.request_id_counter += 1
        new_request = {"id": self.request_id_counter, "description": f"Request {self.request_id_counter}"}
        self.request_queue.put(new_request)
        print(f"New request added: {new_request}")

    def process_request(self):
        """Обробляє заявку з черги, якщо черга не пуста."""
        if not self.request_queue.empty():
            current_request = self.request_queue.get()
            print(f"Processing request: {current_request}")
            time.sleep(random.uniform(0.5, 1.5))  # Імітація часу на обробку заявки
            print(f"Request {current_request['id']} processed successfully.")
        else:
            print("No requests in the queue to process.")

    def run(self):
        """Головний цикл для генерації та обробки заявок."""
        try:
            while True:
                # Генеруємо нову заявку з ймовірністю 50%
                if random.choice([True, False]):
                    self.generate_request()

                # Обробляємо заявку
                self.process_request()

                # Затримка для імітації реального часу
                time.sleep(random.uniform(0.5, 2.0))

        except KeyboardInterrupt:
            print("\nProgram terminated.")

# Запуск системи заявок
if __name__ == "__main__":
    system = RequestSystem()
    system.run()