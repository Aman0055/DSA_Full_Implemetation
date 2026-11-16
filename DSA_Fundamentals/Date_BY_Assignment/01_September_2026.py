"""
# Today's Assignment — Queue

## 🟢 Basic (10)

1. Implement a `Queue` class using a Python list, with `enqueue()`, `dequeue()`, `peek()`, `is_empty()`, and `size()` methods.
2. Implement a `Queue` class using a singly linked list (composition — the queue "has-a" linked list object, with head as front and tail as rear).
3. Implement a `Queue` class by inheriting from a `SinglyLinkedList` class (inheritance-based queue).
4. Write a program to reverse the first `k` elements of a queue while keeping the rest of the order unchanged.
5. Implement a `CircularQueue` class using a fixed-size array, correctly wrapping the `front` and `rear` pointers.
6. Write a program that uses a queue to print numbers from 1 to n in order, dequeuing and printing one at a time.
7. Implement a queue that raises a custom `QueueOverflowError` when `enqueue()` is called on a full fixed-size queue.
8. Write a program to interleave the first half and second half of a queue (e.g., `[1,2,3,4,5,6]` → `[1,4,2,5,3,6]`) using only queue operations.
9. Write a program to check whether two queues contain the same elements in the same order.
10. Implement a `Deque` (double-ended queue) class supporting `add_front()`, `add_rear()`, `remove_front()`, and `remove_rear()`.

## 🟡 Intermediate (8)

1. Implement a stack using two queues, supporting `push()` and `pop()` in amortized O(1) or O(n) depending on your approach.
2. Implement a queue using two stacks, supporting `enqueue()` and `dequeue()` efficiently.
3. Design a "Sliding Window Maximum" solution that finds the maximum in every window of size `k` in an array using a deque.
4. Given a binary tree, implement a level-order traversal (BFS) using a queue, returning a list of lists (one per level).
5. Implement a `Circular Deque` with a fixed capacity supporting insertion/deletion at both ends in O(1) time.
6. Given a queue of integers, write a program to check whether it is sorted in non-decreasing order using only queue operations.
7. Simulate a "Hot Potato" / Josephus-style elimination game using a queue: pass the potato n times, then eliminate the front person, and find the last one remaining.
8. Given two numbers in binary form as strings, generate binary numbers from 1 to n using a queue (BFS-style generation).

## 🔴 Advance (7)

1. Design a task scheduler that processes tasks with cooldown periods between same-type tasks, using a queue-based simulation (Task Scheduler problem).
2. Implement a Least Recently Used (LRU) Cache using a queue (in addition to a hash map) instead of a doubly linked list, and compare the trade-offs.
3. Given a matrix of 0s and 1s representing land and water, use a multi-source BFS (queue-based) to find the distance of each land cell from the nearest water cell.
4. Implement a "Rotten Oranges" style multi-source BFS using a queue to find the minimum time for a condition to propagate through a grid.
5. Design a rate limiter that allows at most `n` requests per sliding time window, using a queue to track timestamps.
6. Given a stream of data, implement a `MovingAverage` class that computes the moving average of the last `k` elements using a queue.
7. Implement a priority queue from scratch (without using `heapq`) using a list or linked list, supporting `insert()` and `extract_min()` in the most efficient way you can justify.
"""