"""
Assignment-10: Stack using Linked List

Import module containing singly linked list code in your python file.
Define a class Stack to implement stack data structure. Define init() method to 
create Singly Linked List (SLL) object.
Define a method is_empty() to check if the stack is empty in Stack class.
In Stack class, define push() method to add data onto the stack.
In Stack class, define pop() method to remove top element from the stack.
In Stack class, define peek() method to return top element on the stack.
In Stack class, define size() method to return size of the stack that is number of 
items present in the stack.
"""
from Single_LinkList_ForBinding import *
# import Single_LinkList_ForBinding as m
# print(m.__file__)
# print(dir(m))

class Stack(SLL):

    def __init__(self):
        self.mylist = SLL()
        self.item_count = 0
    def is_empty(self):
        return self.mylist.is_empty()
    def push(self, data):
        self.mylist.insert_at_start(data)
        self.item_count += 1
    def pop(self):
        if not self.is_empty():
            top_item = self.mylist.start.item
            self.mylist.delete_first()
            self.item_count -= 1
            return top_item
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item
    def size(self):
        return self.item_count

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print("Top elements is :", s.peek())
print("Top element popped :", s.pop())
print("Top element is :", s.peek())
print()