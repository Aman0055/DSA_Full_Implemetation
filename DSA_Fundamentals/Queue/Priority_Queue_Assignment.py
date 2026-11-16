"""
DSA using Python

Assignment-16: Priority queue using list

Define a class PriorityQueue to implement priority queue data structure using list. 
Provide init() method to create a list object (initially empty).
Define a push method in PriorityQueue class to insert new data with given priority.
Define a pop method in PriorityQueue class, which returns the highest priority data 
stored in the priority queue data structure. Raise exception if priority queue is empty.
Define is_empty method in PriorityQueue class to check if the priority queue is empty.
In class PriorityQueue, define a method size to return the number of elements present in the
 priority queue.
"""

class PriorityQueue:
    def __init__(self):
        self.items = []
    def push(self, data, priority):
        index = 0
        while index<len(self.items) and self.items[index][1] <= priority:
            index+=1
        self.items.insert(index,(data, priority))
    def is_empty(self):
        return len(self.items) == 0
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Empty")
        return self.items.pop(0)[0]
    def size(self):
        return len(self.items)
obj = PriorityQueue()
obj.push("Aman", 2)
obj.push("Aditya", 1)
obj.push("Ankit", 3)
obj.push("Aryan",7)
obj.push("Aarav",5)

while not obj.is_empty():
    print(obj.pop())