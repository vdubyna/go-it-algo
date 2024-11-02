class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Вставка в початок списку
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Вставка в кінець списку
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    # Реверсування списку
    def reverse_linked_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Друк списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Вставка в відсортований список
    def sorted_insert(self, new_node):
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    # Сортування списку вставками
    def insertion_sort(self):
        sorted_list = LinkedList()
        current = self.head
        while current:
            next_node = current.next
            sorted_list.sorted_insert(Node(current.data))
            current = next_node
        self.head = sorted_list.head

    # Об'єднання двох відсортованих списків
    def merge_sorted_lists(self, list1, list2):
        dummy = Node()
        tail = dummy
        while list1 and list2:
            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        self.head = dummy.next


# Приклад використання

# Створення списку
llist = LinkedList()
llist.insert_at_end(4)
llist.insert_at_end(2)
llist.insert_at_end(5)
llist.insert_at_end(3)
llist.insert_at_end(1)

print("Оригінальний список:")
llist.print_list()

# Реверсування списку
llist.reverse_linked_list()
print("\nСписок після реверсування:")
llist.print_list()

# Сортування списку
llist.insertion_sort()
print("\nСписок після сортування:")
llist.print_list()

# Об'єднання двох відсортованих списків
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)

merged_list = LinkedList()
merged_list.merge_sorted_lists(list1.head, list2.head)

print("\nОб'єднаний відсортований список:")
merged_list.print_list()