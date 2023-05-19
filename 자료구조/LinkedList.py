class Node:
    def __init__(self, value = 0, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev  # doubled linked list
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:  # O(1)
            self.tail.next = new_node
            self.tail = self.tail.next
        # else:  # O(n) 맨 뒤의 node가 new_node를 가리켜야 한다.
        #     current = self.head
        #     while(current.next):
        #         current = current.next
        #     current.next = new_node
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    def insert_at(self):

    def remove_at(self):

    def insert_back(self):
