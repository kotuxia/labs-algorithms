# Используя словесное описание реализовать работу с очередью

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0) 
        else:
            print("Очередь пуста!")
            return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def size(self):
        return len(self.items)

# Проверка 
q = Queue()

print("Добавляем элементы:")
q.enqueue("Первый")
q.enqueue("Второй")
q.enqueue("Третий")
print(f"Текущая очередь: {q.items}") 

print(f"\nРазмер очереди: {q.size()}")
print(f"Первый в очереди: {q.front()}")

print("\nИзвлекаем элементы:")
print(f"Извлечен: {q.dequeue()}")
print(f"Извлечен: {q.dequeue()}")
print(f"Осталось в очереди: {q.items}") 