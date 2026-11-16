"""
Assignment-13: Queue using Singly Linked List Concept

Q> Define a class Queue to implement queue data structure using singly linked list concept.
 Define __init__() method to initialise front and rear reference variable; and item_count 
 variable to keep track of number of elements in the queue.
Q> Define a method is_empty() to check if the queue is empty in Queue class.
Q> In Queue class, define enqueue() method to add data into the queue.
Q> In Queue class, define dequeue() method to remove front element from the queue.
Q> In Queue class, define get_front() method to return front element of the queue.
Q> In Queue class, define get_rear() method to return rear element of the queue.
Q> In Queue class, define size() method to return size of the queue that is number of
 items present in the queue.
"""
class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next 

class Queue:
    def __init__(self):
        self.front = None
        self.rare = None
        self.item_count = 0
    def is_empty(self):
        return self.front == None
    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rare.next = n
        self.rare = n
        self.item_count += 1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Error Queue")
        elif self.front == self.rare:
            self.front = None
            self.rare = None
        else :
            self.front = self.front.next
        self.item_count -=1 
    def get_front(self):
        if self.is_empty():
            raise IndexError("No data in the queue")
        else :
            return self.front.item 
    def get_rare(self):
        if self.is_empty():
            raise IndexError("No data in the queue")
        else :
            return self.rare.item
    def size(self):
        return self.item_count

q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.get_front(), q1.get_rare())
q1.dequeue()
print(q1.get_front(), q1.get_rare())

    

