"""
Assignment-11: Stack Implementation by extending Singly Linked List

Import module containing singly linked list code in your python file.
Define a class Stack to implement stack data structure by inheriting SLL class.
Define a method is_empty() to check if the stack is empty in Stack class.
In Stack class, define push() method to add data onto the stack.
In Stack class, define pop() method to remove top element from the stack.
In Stack class, define peek() method to return top element on the stack.
In Stack class, define size() method to return size of the stack that is number
of items present in the stack.
"""
from Single_LinkList_ForBinding import *

class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count=0
    def is_empty(self):
        return super().is_empty()
    def push(self, data):
        return self.insert_at_start(data)
        self.item_count += 1
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count -= 1
        else :
            raise IndexError("Stack underflow !")
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else :
            raise IndexError("Stack underflow !")
    def size(self):
        return self.item_count

s1 = Stack()
s1.insert_at_start(10)
s1.insert_at_start(20)
s1.insert_at_start(30)
print("Top element :", s1.peek())
print(s1.pop())
print("Top element :", s1.peek())
print()        