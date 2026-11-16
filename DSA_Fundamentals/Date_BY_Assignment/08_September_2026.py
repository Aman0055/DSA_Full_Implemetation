"""
# Today's Assignment — Binary Trees

## 🟢 Basic (10)

1. Implement a `Node` class (with `data`, `left`, and `right`) and a `BinaryTree` class with an `insert()` method that inserts level by level (like a complete binary tree).
2. Write a method `preorder()` that returns a list of node values using preorder traversal (root → left → right), implemented recursively.
3. Write a method `inorder()` that returns a list of node values using inorder traversal (left → root → right), implemented recursively.
4. Write a method `postorder()` that returns a list of node values using postorder traversal (left → right → root), implemented recursively.
5. Write a method `level_order()` that returns a list of node values using level-order (BFS) traversal, using a queue.
6. Write a method `height()` that returns the height (max depth) of a binary tree, implemented recursively.
7. Write a method `count_nodes()` that returns the total number of nodes in a binary tree.
8. Write a method `count_leaves()` that returns the number of leaf nodes (nodes with no children) in a binary tree.
9. Write a method `find(value)` that returns True/False if a value exists anywhere in the binary tree.
10. Write a method `mirror()` that converts a binary tree into its mirror image by swapping left and right children at every node.

## 🟡 Intermediate (8)

1. Implement a `BinarySearchTree` class with `insert(value)` and `search(value)` methods, maintaining the BST property.
2. Write a method `is_bst()` that checks whether a given binary tree satisfies the Binary Search Tree property.
3. Write a method `delete(value)` for a BST that correctly handles all three cases: leaf node, node with one child, and node with two children.
4. Given a binary tree, write a method to check if it is height-balanced (the height difference between left and right subtrees of every node is at most 1).
5. Write a method `lowest_common_ancestor(n1, n2)` that finds the LCA of two nodes in a Binary Search Tree.
6. Given a binary tree, write a method `level_order_zigzag()` that returns node values in zigzag (alternating left-to-right, right-to-left) level order.
7. Given the preorder and inorder traversal lists of a binary tree, write a function to reconstruct the original binary tree.
8. Write a method `diameter()` that returns the diameter of a binary tree (the length of the longest path between any two nodes, which may or may not pass through the root).

## 🔴 Advance (7)

1. Given a Binary Search Tree, write a method `lowest_common_ancestor(n1, n2)` that works for a general Binary Tree (not just a BST), without assuming any ordering property.
2. Write a method `serialize()` and `deserialize()` for a binary tree, converting it to a string and reconstructing it back into an identical tree.
3. Given a binary tree, write a method to find the maximum path sum between any two nodes (the path doesn't need to pass through the root).
4. Convert a given Binary Search Tree into a sorted Doubly Linked List in-place, without creating any new nodes.
5. Given a binary tree, write a method `right_side_view()` that returns the values visible when the tree is viewed from the right side (topmost node at each level from the right).
6. Implement a self-balancing BST (AVL Tree) with `insert()` that performs the appropriate rotations (LL, RR, LR, RL) to maintain balance after every insertion.
7. Given a binary tree where each node has a value, write a method to find all root-to-leaf paths whose sum equals a given target value.

# Today's Assignment — Stack (Additional)

## 🟢 Basic (10)

1. Write a program to remove all consecutive duplicate characters from a string using a stack (e.g., `"aaabccddd"` → `"abcd"`).
2. Implement a `Stack` class using a single `Queue` internally (push/pop supported entirely through queue operations).
3. Write a program to convert a postfix expression (e.g., `"23*54*+"`) to its equivalent infix expression using a stack.
4. Write a program to convert a prefix expression (e.g., `"*+23*54"`) to its equivalent infix expression using a stack.
5. Write a program to check whether a given arithmetic expression has redundant (unnecessary) parentheses, using a stack.
6. Write a program to find the "Next Smaller Element" for every element in an array (the first smaller element to its right), using a stack.
7. Write a program to delete the middle element of a stack using only recursion (no extra data structure).
8. Implement a stack that supports a `get_size()` method in O(1) time without using Python's `len()` on the underlying list.
9. Write a program to insert an element at the very bottom of a stack using recursion, keeping the rest of the order unchanged.
10. Write a function `is_valid_sequence(pushed, popped)` that checks whether a given `popped` sequence is achievable from a given `pushed` sequence using a single stack.

## 🟡 Intermediate (8)

1. Design a stack that supports `push()`, `pop()`, and `increment(k, val)` (adds `val` to the bottom `k` elements) — implement `increment` in O(1) time.
2. Given a non-negative integer as a string and an integer `k`, use a stack to remove `k` digits so the resulting number is the smallest possible (Remove K Digits).
3. Implement the "Asteroid Collision" problem using a stack: given an array of asteroid sizes/directions, simulate collisions and return the surviving asteroids.
4. Given a simple expression string containing digits and `+`/`-` (no precedence issues), evaluate it using two stacks (one for numbers, one for operators).
5. Implement "Exclusive Time of Functions": given a log of function call/return events, use a stack to compute how much exclusive time each function ran for.
6. Write a program to convert a given postfix expression back into its equivalent prefix expression using a stack.
7. Design a browser-style back/forward history navigator using two stacks (`back_stack` and `forward_stack`), supporting `visit(url)`, `back()`, and `forward()`.
8. Given an array of integers, use a stack to compute the sum of the minimum element of every possible contiguous subarray (Sum of Subarray Minimums).

## 🔴 Advance (7)

1. Implement "Basic Calculator II" — evaluate a string expression containing `+`, `-`, `*`, `/` and non-negative integers (respecting precedence) using a stack, without `eval()`.
2. Implement the "132 Pattern" problem: given an array, use a stack to determine whether there exists a subsequence `i < j < k` such that `a[i] < a[k] < a[j]`.
3. Solve the "Celebrity Problem" (given a matrix of who-knows-whom relationships, find the celebrity known by everyone but who knows no one) using a stack-based approach.
4. Implement the "Stock Span Problem": for each day's stock price, use a stack to compute the number of consecutive previous days the price was less than or equal to today's price.
5. Write a stack-based parser that validates and evaluates simple nested ternary expressions (e.g., `"T?2:3"`, `"F?1:T?4:5"`).
6. Implement "Minimum Remove to Make Valid Parentheses": given a string with letters and parentheses, use a stack to remove the minimum number of parentheses to make it valid.
7. Given a binary matrix, use a stack-based histogram approach (row by row) to find the area of the largest rectangle containing only 1s (Maximal Rectangle problem).

# Today's Assignment — Queue (Additional)

## 🟢 Basic (10)

1. Implement a `Queue` class using a fixed-size Python list with `front` and `rear` index pointers, avoiding costly shifting on dequeue.
2. Write a program that uses a queue to generate the first `n` "ugly numbers" (numbers whose only prime factors are 2, 3, or 5).
3. Implement a simple `PriorityQueue` class using a sorted list, supporting `insert(value, priority)` and `pop_min()`.
4. Write a program to reverse a queue completely using recursion (no additional queue or stack allowed as a helper data structure).
5. Implement a `Queue` class that supports `get_front()` and `get_rear()` lookups in O(1) time without removing elements.
6. Write a program to check whether the elements of a queue can be rearranged into sorted order using only one auxiliary stack.
7. Implement a queue-like structure that supports `get_max()` in O(1) amortized time using an auxiliary max-deque.
8. Write a program to find the first negative number in every window of size `k` in an array using a deque.
9. Write a program that uses a queue to generate the first `n` binary-representable numbers made only of digits `0` and `1` (treated as decimal-looking numbers, e.g., 1, 10, 11, 100...).
10. Implement a `CircularBuffer` class with a fixed capacity that overwrites the oldest element once full.

## 🟡 Intermediate (8)

1. Design a simplified "Snake Game" where the snake's body is represented using a deque, supporting `move(direction)`.
2. Implement LeetCode-style "Design Circular Queue" with `enqueue()`, `dequeue()`, `front()`, `rear()`, `is_empty()`, and `is_full()` methods.
3. Implement a "Hit Counter" / "Number of Recent Calls" class using a queue that tracks how many events occurred within the last 3000 milliseconds (or last `t` units).
4. Implement a `dequeue_all_matching(value)` method on a queue that removes every occurrence of `value` while preserving the relative order of remaining elements, in O(n) time.
5. Given a set of tasks with arrival times and burst times, use a queue to simulate First-Come-First-Served (FCFS) CPU scheduling and compute average waiting time.
6. Implement a basic two-level Multi-Level Feedback Queue (MLFQ) simulation using two queues of different priority/time-slice.
7. Given a grid of rooms/cells (0s and 1s), use BFS with a queue to determine whether all reachable cells can be visited from a given source cell (flood fill).
8. Given a matrix representing a maze, use a queue-based BFS to find the shortest path length from a start cell to an end cell.

## 🔴 Advance (7)

1. Design a "Print Queue Simulation" where print jobs have priorities, and higher-priority jobs are always dequeued first (priority queue over a regular queue).
2. Solve the "01 Matrix" problem: given a matrix of 0s and 1s, find the distance of the nearest 0 for every cell using multi-source BFS with a queue.
3. Solve the "Open the Lock" problem using BFS with a queue: find the minimum number of turns to reach a target combination while avoiding a set of "deadend" combinations.
4. Implement a Sliding Window Median using a deque to track window indices alongside two heaps for the median calculation.
5. Solve the "Walls and Gates" problem: given a grid of walls, gates, and empty rooms, use multi-source BFS with a queue to fill each empty room with its distance to the nearest gate.
6. Design a bounded Producer-Consumer simulation using a queue with limited capacity, where producers block (or wait) when the queue is full and consumers block when it's empty.
7. Implement 0-1 BFS using a deque (elements added to the front for 0-weight edges and to the back for 1-weight edges) to find shortest paths in a graph with only 0/1 edge weights.
"""