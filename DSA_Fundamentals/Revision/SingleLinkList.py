class Node:
    def __init__(self, items= None, next=None):
        self.items = items
        self.next = next
class SLL:
    def __init__(self, start = None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n
    def insert_at_last(self, data):
        n = Node(data,self.start)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n
    def size(self):
        return len(Node)
obj = SLL()
print(obj.insert_at_start(34))
print(obj.insert_at_last(90))
print(obj.insert_at_start(36))
print(obj.is_empty())
print(obj.size())

            
                    