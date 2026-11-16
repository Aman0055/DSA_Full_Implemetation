"""
Assignment-17: Priority queue using linked list

Define a Node class with instance member variables item, priority and next.
Define a class PriorityQueue to implement priority queue data structure using 
singly linked list. Provide init() method to create a start reference variable 
(initially containing None) and item_count variable (initially 0).
Define a push method in PriorityQueue class to insert new data with given priority.
Define a pop method in PriorityQueue class, which returns the highest priority data stored
 in the priority queue data structure. Raise exception if priority queue is empty.
Define is_empty method in PriorityQueue class to check if the priority queue is empty.
In class PriorityQueue, define a method size to return the number of elements present in
 the priority queue.
"""
class Node:
    def __init__(self, items=None, priority=None, next=None):
        self.items = items
        self.priority = priority
        self.next = next
class PriorityQueue:
    def __init__(self):
        self.start = None
        self.items_count = 0
    def push(self, data, priority):
        n = Node(data,priority)
        if not self.start or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.items_count += 1
    def is_empty(self):
        return self.start == None
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        data = self.start.items
        self.start = self.start.next
        self.items_count -= 1
        return data
    def size(self):
        return self.items_count
    
obj = PriorityQueue()
obj.push("Aman", 2)
obj.push("Aditya", 1)
obj.push("Ankit", 3)
obj.push("Aryan",7)
obj.push("Aarav",5)

while not obj.is_empty():
    print(obj.pop())