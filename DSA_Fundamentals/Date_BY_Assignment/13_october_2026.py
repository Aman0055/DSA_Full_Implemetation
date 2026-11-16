"""
# Today's Assignment — 50 New Questions (Beginner to Intermediate)
Topics: Stack, Queue, Bubble / Selection / Insertion / Merge Sort, Heap, Graph, Tree
(None of these repeat the questions from the earlier assignment files.)


# Stack

## 🟢 Basic

1. Baseball Game: given a list of operations like `["5","2","C","D","+"]`, use a stack to compute the total score. An integer adds that score, `+` adds the sum of the last two scores, `D` doubles the last score, and `C` cancels (removes) the last score.
2. Crawler Log Folder: given logs like `["d1/","d2/","../","d21/","./"]`, use a stack to find the minimum number of steps needed to return to the main folder (`../` goes up one level, `./` stays, `x/` goes into a folder).
3. Remove Outermost Parentheses: given a valid parentheses string like `"(()())(())"`, remove the outermost parentheses of every primitive part using a stack (or a depth counter) and return `"()()()"`.

## 🟡 Intermediate

4. Make The String Great: repeatedly remove two adjacent characters that are the same letter in different cases (e.g., `"aA"`) using a stack, e.g., `"leEeetcode"` becomes `"leetcode"`.
5. Asteroid Collision: given an array where positive values move right and negative values move left (the absolute value is the size), use a stack to simulate collisions (the smaller one explodes, equal sizes both explode) and return the survivors.
6. Online Stock Span: design a class `StockSpanner` with `next(price)` that returns the number of consecutive previous days (including today) whose price was less than or equal to today's price, using a stack.


# Queue

## 🟢 Basic

7. Implement a `Queue` using a singly linked list with `front` and `rear` pointers so that both `enqueue()` and `dequeue()` run in O(1) time.
8. Recent Counter: design a class with `ping(t)` that returns how many requests arrived in the last 3000 milliseconds (the range `[t-3000, t]`), using a queue.
9. Bank Counter Simulation: given customers as `(arrival_time, service_time)` pairs and a single counter, use a queue to compute each customer's waiting time and the average waiting time.

## 🟡 Intermediate

10. Implement a Priority Queue using a plain list where `enqueue(item, priority)` keeps the list ordered and `dequeue()` always returns the highest-priority item. State the time complexity of each operation.
11. Reveal Cards In Increasing Order: given a deck of numbers, find the ordering that, when you repeatedly reveal the top card and move the next top card to the bottom, reveals the cards in increasing order (use a queue of indexes).
12. Design Circular Deque: implement a deque using a fixed-size array with `insert_front`, `insert_last`, `delete_front`, `delete_last`, `get_front`, `get_rear`, `is_full`, and `is_empty`, handling wrap-around with modulo.


# Bubble Sort

## 🟢 Basic

13. Implement an optimized Bubble Sort with a `swapped` flag that stops early when a pass makes no swaps, and print how many passes were actually needed for a sorted, a reverse-sorted, and a random array.
14. Print the array after every pass of Bubble Sort, and mark which elements are already in their final position after each pass.

## 🟡 Intermediate

15. Implement Cocktail Shaker Sort (bidirectional Bubble Sort) that bubbles the largest to the right and then the smallest to the left in every round, and compare its number of passes with normal Bubble Sort on `[2, 3, 4, 5, 1]`.


# Selection Sort

## 🟢 Basic

16. Use Selection Sort to sort a list of `(name, age)` tuples by age, and by name when the ages are equal.
17. Implement Selection Sort that counts the number of comparisons and swaps, and show that swaps are at most `n - 1` while comparisons are always `n(n-1)/2`. Compare this with your Bubble Sort counts.

## 🟡 Intermediate

18. Standard Selection Sort is not stable. Show this with an example (like `[(4,'a'), (4,'b'), (2,'c')]`), then write a stable version that shifts elements instead of swapping them.


# Insertion Sort

## 🟢 Basic

19. Implement Insertion Sort in descending order and print the array after inserting each element, along with the number of shifts that insertion needed.
20. Sort a list of student records `(name, marks)` by marks in descending order using Insertion Sort, keeping students with equal marks in their original order.

## 🟡 Intermediate

21. Implement Binary Insertion Sort, which uses binary search to find the insertion position. Explain which cost improves (comparisons or shifts) and which stays the same.


# Merge Sort

## 🟢 Basic

22. Write a `merge(a, b)` function that merges two sorted lists into one sorted list and removes duplicates while merging (the "sorted union").
23. Implement top-down Merge Sort that prints each split and each merge with indentation showing the recursion depth.

## 🟡 Intermediate

24. Implement bottom-up (iterative) Merge Sort that merges sub-arrays of size 1, 2, 4, 8, ... without any recursion.
25. Merge K sorted lists into one sorted list using the divide-and-conquer approach (merge the lists pairwise, round by round), and state the time complexity.


# Heap

## 🟢 Basic

26. Implement a `MinHeap` class using an array with `insert()`, `get_min()`, and `extract_min()`, using the formulas `2i+1`, `2i+2`, and `(i-1)//2`.
27. Build a Max Heap from an unsorted array using the bottom-up `heapify` approach (start from the last non-leaf node) and explain why this takes O(n) and not O(n log n).
28. Implement Heap Sort for ascending order using a Max Heap, and print the heap after each extraction.
29. Find the Kth largest element in an array using a min-heap of size `k` (use `heapq`).

## 🟡 Intermediate

30. Last Stone Weight: repeatedly smash the two heaviest stones together (equal stones vanish, otherwise the difference remains) until at most one stone is left, using a max-heap.
31. Top K Frequent Elements: given an array and `k`, return the `k` most frequent elements using a hash map and a heap.
32. K Closest Points to Origin: given a list of `(x, y)` points, return the `k` points closest to `(0, 0)` using a heap.
33. Find Median from Data Stream: design a class with `add_num(n)` and `find_median()` using two heaps (a max-heap for the lower half and a min-heap for the upper half).


# Graph

## 🟢 Basic

34. Implement a `Graph` class using an adjacency list (dictionary of lists) with `add_vertex()`, `add_edge(u, v)` that works for both directed and undirected graphs, and `display()`.
35. Represent a graph using an adjacency matrix, and write functions to print the degree of every vertex (in-degree and out-degree for a directed graph).
36. Implement Breadth-First Search (BFS) from a given source vertex using a queue and print the visiting order.
37. Implement Depth-First Search (DFS) both recursively and iteratively (using a stack), and print the visiting order for the same graph.
38. Find If Path Exists in Graph: given `n` vertices, a list of edges, a source, and a destination, return whether a path exists between them.

## 🟡 Intermediate

39. Count the number of connected components in an undirected graph, and print the vertices of each component.
40. Number of Islands: given a 2D grid of `'1'` (land) and `'0'` (water), count the islands using DFS or BFS (land connects in 4 directions only).
41. Detect a cycle in an undirected graph using DFS (keep track of the parent vertex to avoid false cycles).
42. Check whether a graph is bipartite by colouring it with two colours using BFS (a graph with an odd-length cycle is not bipartite).


# Tree

## 🟢 Basic

43. Implement a `Node` class (`data`, `left`, `right`), build a small binary tree by hand, and write recursive `preorder()`, `inorder()`, and `postorder()` traversals.
44. Implement Level Order Traversal using a queue, and print each level on its own line.
45. Write functions to find the height (maximum depth) of a binary tree, count the total nodes, and count the leaf nodes.
46. Implement a Binary Search Tree (BST) class with `insert(value)` and `search(value)`, and verify that its inorder traversal prints a sorted sequence.

## 🟡 Intermediate

47. Invert (mirror) a binary tree, and also write a function to check whether a binary tree is symmetric around its centre.
48. Path Sum: given a binary tree and a target sum, check whether any root-to-leaf path adds up to the target, and then print all such paths.
49. Validate Binary Search Tree: check whether a given binary tree is a valid BST, using the min/max range approach (not just comparing each node with its immediate children).
50. Find the Lowest Common Ancestor (LCA) of two nodes in a BST by using the BST property, without searching the whole tree.
"""