"""
# Today's Assignment — Singly Linked List

## 🟢 Basic (10)

1. Implement a `Node` class (with `data` and `next`) and a `SinglyLinkedList` class with `insert_at_end()` and `display()` methods.
2. Write a method `insert_at_beginning()` to add a node at the head of a singly linked list.
3. Write a method `get_length()` that returns the total number of nodes without using a counter passed as a parameter.
4. Write a method `search(value)` that returns True/False if a value exists in the list.
5. Write a method `delete_first()` to remove the head node of a singly linked list.
6. Write a method `delete_last()` to remove the tail node of a singly linked list.
7. Write a method `insert_at_position(index, value)` to insert a node at a given index.
8. Write a method `delete_at_position(index)` to delete a node at a given index.
9. Write a method to find the sum and average of all node values in a singly linked list of integers.
10. Write a method `insert_after_value(target, value)` that inserts a new node right after the node containing `target`.

## 🟡 Intermediate (8)

1. Reverse a singly linked list iteratively (changing `next` pointers in a single pass).
2. Find the middle node of a singly linked list using the slow/fast pointer technique.
3. Check whether a singly linked list is a palindrome (using the slow/fast pointer technique to find the middle).
4. Detect if a singly linked list has a cycle using Floyd's Cycle Detection algorithm.
5. Remove all duplicate values from an unsorted singly linked list.
6. Find the N-th node from the end of a singly linked list in a single traversal (without computing length first).
7. Given two singly linked lists representing numbers (digit by digit), add them and return the result as a new linked list.
8. Rotate a singly linked list to the right by `k` places.

## 🔴 Advance (7)

1. Reverse a singly linked list recursively, and explain what happens on the call stack at each level.
2. Reverse a singly linked list in groups of `k` nodes (e.g., reverse every 3 nodes) and connect the groups back together.
3. Merge two sorted singly linked lists into one sorted singly linked list without using extra array storage.
4. Given a singly linked list with a cycle, find the exact node where the cycle begins (not just whether a cycle exists).
5. Given a singly linked list with a cycle, remove the cycle so the list becomes a proper NULL-terminated list, without losing any nodes.
6. Flatten a multilevel singly linked list where some nodes have an additional `child` pointer to another linked list, into a single-level list.
7. Find the intersection point of two singly linked lists (where they merge into one), without using extra space.

# Today's Assignment — Doubly Linked List

## 🟢 Basic (10)

1. Implement a `Node` class (with `data`, `next`, and `prev`) and a `DoublyLinkedList` class with `insert_at_end()` and `display()` (forward direction) methods.
2. Write a method `insert_at_beginning()` for a doubly linked list, making sure both `next` and `prev` pointers are updated correctly.
3. Write a method `display_reverse()` that traverses and prints a doubly linked list from tail to head using the `prev` pointers.
4. Write a method `count_nodes()` that returns the total number of nodes in a doubly linked list.
5. Write a method `search(value)` to check whether a value exists in a doubly linked list.
6. Write a method to delete the first node (head) of a doubly linked list, correctly updating the new head's `prev` pointer.
7. Write a method to delete the last node (tail) of a doubly linked list, correctly updating the new tail's `next` pointer.
8. Write a method `get_node_at(index)` that returns the node at a given position, traversing from whichever end (head or tail) is closer.
9. Write a method `insert_before_value(target, value)` that inserts a new node right before the node containing `target`.
10. Write a method `to_list()` that converts a doubly linked list into a plain Python list.

## 🟡 Intermediate (8)

1. Write a method `insert_at_position(index, value)` for a doubly linked list, correctly linking both `next` and `prev` pointers of neighboring nodes.
2. Write a method to delete a node by value from a doubly linked list (handle head, tail, and middle cases separately).
3. Remove duplicate values from a doubly linked list while preserving the order of first occurrence.
4. Reverse a doubly linked list in-place by swapping `next` and `prev` at every node (and updating the head pointer).
5. Implement `delete_node(node_reference)` in O(1) given a direct reference to the node (not the head), leveraging the `prev` pointer.
6. Find the middle node of a doubly linked list using the slow/fast pointer technique.
7. Check whether a doubly linked list is a palindrome using the `prev` and `next` pointers from both ends.
8. Convert a given singly linked list into a doubly linked list in-place (constructing correct `prev` pointers throughout).

## 🔴 Advance (7)

1. Implement a basic LRU (Least Recently Used) Cache using a doubly linked list + hash map, supporting `get(key)` and `put(key, value)` in O(1) time.
2. Given a doubly linked list where each node also has a `child` pointer to another doubly linked list, flatten it into a single-level doubly linked list.
3. Given a doubly linked list, sort it (e.g., using merge sort adapted for doubly linked lists) without converting it to an array first.
4. Implement a Least Frequently Used (LFU) Cache using a doubly linked list based structure.
5. Merge two sorted doubly linked lists into one sorted doubly linked list in-place.
6. Given a doubly linked list, rotate it to the right by `k` places without losing any `prev`/`next` links.
7. Design a "browser history" system using a doubly linked list supporting `visit(url)`, `back(steps)`, and `forward(steps)`.

# Today's Assignment — Circular Linked List

## 🟢 Basic (10)

1. Implement a `Node` class and a `CircularLinkedList` class with `insert_at_end()` that correctly links the last node back to the head.
2. Write a method `insert_at_beginning()` for a circular linked list, making sure the new head's `next` still points back correctly and the old last node updates too.
3. Write a method `display()` for a circular linked list that prints all nodes exactly once (careful not to loop forever).
4. Write a method `count_nodes()` that returns the total number of nodes in a circular linked list.
5. Write a method `search(value)` that returns True/False if a value exists in a circular linked list.
6. Write a method to delete the first node of a circular linked list, correctly re-linking the last node to the new head.
7. Write a method to delete the last node of a circular linked list, correctly updating the new last node's `next` pointer.
8. Write a method `sum_of_nodes()` that returns the sum of all node values in a circular linked list.
9. Write a method `find_max()` and `find_min()` to return the largest and smallest values in a circular linked list.
10. Write a method `to_list()` that converts a circular linked list into a plain Python list, traversing exactly once.

## 🟡 Intermediate (8)

1. Write a method `insert_at_position(index, value)` to insert a node at a given index in a circular linked list.
2. Write a method to delete a node by value from a circular linked list (handle the case where it's the only node, the head, or the tail).
3. Split a circular linked list into two halves, each forming its own circular linked list.
4. Convert a given singly linked list into a circular linked list in-place (link the last node back to the head).
5. Detect whether a given linked list (passed without any "is circular" flag) is actually circular or a normal NULL-terminated list.
6. Reverse a circular linked list in-place, keeping it circular after the reversal.
7. Given two circular linked lists, merge them into a single circular linked list.
8. Find the middle node of a circular linked list using the slow/fast pointer technique (careful with the loop termination condition).

## 🔴 Advance (7)

1. Solve the Josephus Problem using a circular linked list: given `n` people in a circle and every `k`-th person eliminated, find the last remaining person.
2. Given a circular linked list, find the starting node of the loop if it were merged into a bigger list at an unknown point (i.e., locate the "junction" node).
3. Implement a circular doubly linked list (each node has `next` and `prev`, and the list wraps in both directions) supporting O(1) insertion and deletion at both ends.
4. Implement a round-robin CPU scheduler simulation using a circular linked list, where each process gets a fixed time slice before moving to the next.
5. Given a circular linked list, sort it without breaking circularity, and without converting it to an array first.
6. Design a "Josephus Problem" variant where survivors must also be returned in the order they were eliminated, using a circular linked list.
7. Given a circular linked list representing a playlist, implement `shuffle()` and `next_track()` methods that respect O(1) time where possible.

# Today's Assignment — Stack

## 🟢 Basic (10)

1. Implement a `Stack` class using a Python list, with `push()`, `pop()`, `peek()`, `is_empty()`, and `size()` methods.
2. Implement a `Stack` class using a singly linked list (composition — the stack "has-a" linked list object).
3. Implement a `Stack` class by inheriting from a `SinglyLinkedList` class (inheritance-based stack).
4. Write a program to reverse a string using a stack.
5. Write a program to check whether a given string of parentheses `()`, `{}`, `[]` is balanced using a stack.
6. Write a program to convert a decimal number to its binary representation using a stack.
7. Write a program that uses a stack to check whether a given string is a palindrome.
8. Implement a stack that raises a custom `StackUnderflowError` when `pop()` or `peek()` is called on an empty stack.
9. Write a program to reverse the elements of a stack using only stack operations (no extra array), using recursion.
10. Write a program to print the elements of a stack in sorted order using only one additional stack (no arrays or lists).

## 🟡 Intermediate (8)

1. Implement a function to evaluate a postfix expression (e.g., `"23*54*+"`) using a stack.
2. Convert an infix expression (e.g., `"(a+b)*c"`) to postfix notation using a stack, respecting operator precedence.
3. Implement a "Next Greater Element" function for an array using a stack, where each element is replaced by the next greater element to its right.
4. Design a stack that supports `push()`, `pop()`, `top()`, and `get_min()` — all in O(1) time (Min Stack problem).
5. Implement two stacks in a single array such that neither overflows until the array is completely full.
6. Write a program to sort a stack in ascending order using only recursion (no extra data structure).
7. Given a string containing digits and brackets like `"3[a2[c]]"`, decode it into `"accaccacc"`-style expanded strings using a stack.
8. Implement a stack-based solution to check if a sequence of pushed and popped values is valid for a given push order (Validate Stack Sequences).

## 🔴 Advance (7)

1. Implement a stack that supports `push()`, `pop()`, and `get_max()` all in O(1) time and O(1) extra space (without a second stack).
2. Given an array of daily temperatures, use a stack to find, for each day, how many days you'd have to wait until a warmer temperature (Daily Temperatures problem).
3. Given a histogram represented by an array of bar heights, find the area of the largest rectangle that can be formed using a stack-based approach.
4. Implement a basic calculator that evaluates a string expression containing `+`, `-`, parentheses, and non-negative integers, using a stack (no `eval()`).
5. Design and implement a stack-based undo/redo mechanism for a simple text editor (two stacks: undo stack and redo stack).
6. Given an array representing elevation/heights, calculate how much rainwater can be trapped between the bars using a stack-based approach (Trapping Rain Water via Stack).
7. Implement the Largest Rectangle in a Binary Matrix problem by reducing each row to a histogram and reusing the "Largest Rectangle in Histogram" stack technique.
"""