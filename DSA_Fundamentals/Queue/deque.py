"""
* Variations of deque 
* What is a deque ?
* Operations on deque ?
* Implementation of deque ?

Variations of Queue
____________________

• Insertion restricted

          insertion
             ↓
        Rear/back                    Front
          ↙                           ↘
       delete                        delete
   ┌─────────────────────────────┐
   │                             │
   └─────────────────────────────┘


• Deletion restricted

          insertion
             ↓
        Rear/back                    Front
          ↙                           ↘
       insertion                     delete
   ┌─────────────────────────────┐
   │                             │
   └─────────────────────────────┘

*************************************************************************************************
Deque
______

• Deque is another variation of queue

• Deque is Double - Ended - Queue

• Deque is a linear data structure

• Both ends can be used for insertion
  and deletion

        Insertion →  Rear/back              Front  ← Insertion
                    ┌──────────────────────────┐
                    │                          │
                    └──────────────────────────┘
        Delete     ←                              →  Delete

• Some deques may support random
  access, depending on implementation

  
* Operations On Deque :
insert-front 
insert-rare 
delete-front
delete-rare
get-front
get-rare
is_empty
size


* Implementation of Deque :
1> Using list 
2> By extending list class 
3> Using doubly linked list class
4> By extending doubly linked list class
5> Using linked list concepts 
"""
