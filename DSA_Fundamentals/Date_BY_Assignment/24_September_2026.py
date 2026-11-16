"""
# Today's Assignment — OOPs

## 🟢 Basic (7)

1. Create a `Laptop` class with `brand`, `ram`, and `price`. Implement both `__str__` (user-friendly output) and `__repr__` (developer-friendly output) and show where each one is used.
2. Create a `Point` class with `x` and `y`. Add methods `distance_from_origin()` and `distance_to(other_point)`.
3. Create a `Thermometer` class where `celsius` is a `@property` with a setter that rejects any value below -273.15 by raising a `ValueError`.
4. Create a `Pizza` class with `size` and `toppings`. Add `@classmethod` alternative constructors `margherita()` and `pepperoni()` that return pre-configured objects.
5. Create a `Song` class and a `Playlist` class where the playlist "has-a" list of songs (composition). Add `add_song()` and `total_duration()` methods.
6. Create a `FileHandler` class that prints a message in `__del__` when the object is destroyed. Demonstrate it using `del` and by letting the object go out of scope.
7. Explain the difference between `is` and `==` for objects. Show it with a `Token` class, first without and then with `__eq__` defined.

## 🟡 Intermediate (5)

1. Create a `Fraction` class that stores a numerator and denominator, reduces itself using `math.gcd`, and supports `+`, `*`, and `__str__` through operator overloading.
2. Create a `Deck` class (a deck of playing cards) that supports `len(deck)`, `deck[i]` indexing, and iteration using `for card in deck` by implementing `__len__`, `__getitem__`, and `__iter__`.
3. Write a `JSONSerializableMixin` with a `to_json()` method, and combine it with an `Invoice` class using multiple inheritance. Explain why mixins are useful.
4. Create an `Employee` class using `@dataclass` with a default list field (`field(default_factory=list)`), `order=True`, and then a second `frozen=True` version. Show what happens when you try to modify the frozen one.
5. Create a `Multiplier` class whose objects are callable (using `__call__`), e.g., `double = Multiplier(2); double(5)` gives `10`. Compare this approach with a closure-based solution.

## 🔴 Advance (3)

1. Implement the Observer design pattern: a `NewsAgency` (subject) that notifies multiple `Subscriber` objects (observers) whenever a new headline is published, with `subscribe()` and `unsubscribe()` support.
2. Design a "Parking Lot System" using OOP — classes for `Vehicle` (Bike, Car, Truck), `ParkingSlot`, `Ticket`, and `ParkingLot`, with slot allocation by vehicle size and a fee calculation on exit.
3. Use `__init_subclass__` (or a metaclass) to build a plugin registry: every subclass of a base `Plugin` class should automatically register itself in a dictionary by name, without any manual registration code.


# Today's Assignment — Exception Handling

## 🟢 Basic (7)

1. Write a program that tries to add an integer and a string, handles the `TypeError`, and then shows the corrected version of the code.
2. Write a program that handles `AttributeError` when a method is called on `None` (for example, on the result of a failed lookup function).
3. Write a program that tries to import a module and falls back to an alternative if `ImportError` occurs (e.g., try `ujson`, fall back to `json`).
4. Write a program that deliberately triggers infinite recursion and catches the resulting `RecursionError` gracefully.
5. Write a program that runs a list of risky operations and, for each failure, prints the exception's class name (`type(e).__name__`) and its message.
6. Write a program that uses `except (ValueError, TypeError) as e:` (tuple form) to parse inputs like `"10"`, `"abc"`, `None`, and `[5]` into integers.
7. Write a program that calls `next()` on an exhausted iterator, handles `StopIteration`, and then shows the same call using the `default` argument.

## 🟡 Intermediate (5)

1. Write a function `get_valid_age()` that keeps asking for input in a loop until the user enters a valid integer between 1 and 120, handling each kind of error with a different message.
2. Create a custom `ValidationError` that stores the `field_name` and `value` that failed, overrides `__str__`, and use it in a user-registration function.
3. Use `contextlib.suppress(FileNotFoundError)` to delete a file that may not exist. Compare it with an equivalent `try/except/pass` block and explain when each is preferable.
4. Demonstrate the `traceback` module: use `traceback.format_exc()` to capture an error as a string and `traceback.print_exc()` to print it, from inside an `except` block.
5. Demonstrate the difference between a bare `raise` and `raise e` inside an `except` block, and show how each affects the traceback.

## 🔴 Advance (3)

1. Simulate three concurrent tasks that fail with different exceptions, collect them into an `ExceptionGroup`, and handle them separately using `except*` (Python 3.11+).
2. Implement a `Result` pattern: write a decorator `@safe` that wraps a function so it never raises, and instead returns an object with `.ok`, `.value`, and `.error` fields.
3. Implement a `CircuitBreaker` class that opens after `n` consecutive failures and raises a custom `CircuitOpenError` immediately for further calls until a cooldown period has passed, after which it allows a trial call.


# Today's Assignment — Arrays

## 🟢 Basic (7)

1. Find the third largest distinct element in an array without sorting the whole array.
2. Find the union and intersection of two arrays (without using Python's `set` operators).
3. Shift all elements of an array one position to the right (the last element moves to the front) and then one position to the left.
4. Check whether two arrays contain exactly the same elements with the same frequencies, regardless of order.
5. Count the number of elements in an array that appear exactly once.
6. Create a "running maximum" array where each position holds the maximum of all elements up to that index.
7. Find the indices of the maximum and minimum elements in an array and swap those two elements.

## 🟡 Intermediate (5)

1. Given an array, return a new array where each element is the product of all other elements, without using division (Product of Array Except Self).
2. Given an array of non-negative integers and a target sum, find a contiguous subarray that adds up to the target using the sliding window technique.
3. Given a list of intervals like `[[1,3],[2,6],[8,10],[9,12]]`, merge all overlapping intervals.
4. In an array where every element appears twice except one, find the single element using XOR in O(n) time and O(1) space.
5. Rearrange an array into wave form so that `arr[0] >= arr[1] <= arr[2] >= arr[3] ...`.

## 🔴 Advance (3)

1. Find the smallest missing positive integer in an unsorted array in O(n) time and O(1) extra space (First Missing Positive).
2. Count the number of contiguous subarrays whose sum equals `k` (the array can contain negative numbers) using prefix sums and a hash map.
3. Find the median of two sorted arrays in O(log(min(n, m))) time using binary search on the partition.


# Today's Assignment — Strings

## 🟢 Basic (7)

1. Remove all vowels from a given string.
2. Swap the case of every character in a string (upper ↔ lower) manually, without using `.swapcase()`.
3. Find the longest word in a sentence and print its length.
4. Check whether a given sentence is a pangram (contains every letter of the English alphabet at least once).
5. Count how many times a substring occurs in a string, including overlapping occurrences (e.g., `"aa"` in `"aaaa"` → 3), without using `.count()`.
6. Remove duplicate characters from a string while preserving the order of first appearance.
7. Check whether a string is a valid variable name (starts with a letter or underscore, and contains only letters, digits, and underscores) without using `.isidentifier()`.

## 🟡 Intermediate (5)

1. Implement your own `my_atoi(s)` that converts a string to an integer, handling leading spaces, an optional sign, invalid characters, and 32-bit overflow.
2. Find the longest common prefix among a list of strings (e.g., `["flower","flow","flight"]` → `"fl"`).
3. Check whether two strings are isomorphic (each character in one maps to exactly one character in the other, e.g., `"egg"` and `"add"`).
4. Add two very large non-negative numbers given as strings and return the result as a string, without converting them to `int`.
5. Reverse only the vowels in a string while keeping all other characters in their original positions.

## 🔴 Advance (3)

1. Implement the KMP (Knuth-Morris-Pratt) algorithm by building the LPS (longest proper prefix-suffix) table, and use it to find all occurrences of a pattern in a text.
2. Find the length of the Longest Common Subsequence of two strings, and also reconstruct and print the subsequence itself.
3. Given strings `s` and `t`, find the smallest window in `s` that contains all characters of `t` (Minimum Window Substring).


# Today's Assignment — Singly Linked List

## 🟢 Basic (7)

1. Add `__len__`, `__iter__`, and `__str__` (e.g., `1 -> 2 -> 3 -> None`) to your `SinglyLinkedList` class so it works with `len()`, `for` loops, and `print()`.
2. Write `get_at(index)` and `update_at(index, value)` methods, with support for negative indexes (e.g., `-1` means the last node).
3. Write `from_list(python_list)` and `to_list()` methods to convert between a Python list and a singly linked list.
4. Write a method to find the node holding the maximum value and the node holding the minimum value.
5. Write a method `count_occurrences(value)` that returns how many times a value appears in the list.
6. Write a method `delete_all(value)` that deletes every node containing the given value (watch out for the head being deleted repeatedly).
7. Write a function that checks whether two singly linked lists are identical (same values in the same order).

## 🟡 Intermediate (5)

1. Swap two nodes given their values by changing the links (not the data), handling the cases where one of them is the head or where they are adjacent.
2. Swap every two adjacent nodes in a singly linked list by changing links, not values (Swap Nodes in Pairs).
3. Partition a linked list around a value `x` so that all nodes less than `x` come before nodes greater than or equal to `x`, preserving the original relative order.
4. Rearrange a linked list so that all nodes at even values come after all odd-valued nodes, preserving relative order in each group.
5. Sort a singly linked list using insertion sort, building a new sorted list node by node.

## 🔴 Advance (3)

1. Sort a singly linked list in O(n log n) time using merge sort (find the middle, split, sort each half, and merge).
2. Reorder a list `L0 → L1 → ... → Ln` into `L0 → Ln → L1 → Ln-1 → L2 → ...` in-place, without changing node values.
3. Deep copy a linked list where each node has an extra `random` pointer that may point to any node in the list (or `None`), in O(n) time.


# Today's Assignment — Doubly Linked List

## 🟢 Basic (7)

1. Add `__len__`, `__iter__`, and `__reversed__` methods to your `DoublyLinkedList` class so it supports `len()`, forward iteration, and `reversed()`.
2. Write a method `insert_after_value(target, value)` that inserts a new node right after the node containing `target`, correctly updating the `prev` of the following node.
3. Write methods to find the maximum and minimum value in a doubly linked list.
4. Maintain both `head` and `tail` pointers and write `from_list(python_list)` so that building a list of n items takes O(n) total time.
5. Write a method `delete_at_position(index)` that deletes the node at a given index, handling head, tail, and middle cases.
6. Write a method that returns the sum of all node values and the count of even values in a doubly linked list.
7. Write `is_empty()` and `clear()` methods, where `clear()` also breaks every node's `prev`/`next` link so nothing is left dangling.

## 🟡 Intermediate (5)

1. Given a sorted doubly linked list of distinct positive integers, find all pairs whose sum equals a given value using two pointers (one from each end).
2. Delete all occurrences of a given key from a doubly linked list.
3. Swap every two adjacent nodes in a doubly linked list by re-linking `next` and `prev` (not by swapping data).
4. Split a doubly linked list into two halves, giving two independent, correctly terminated doubly linked lists.
5. Insert a value into a sorted doubly linked list so that the list stays sorted (handle insertion at head, tail, and middle).

## 🔴 Advance (3)

1. Given a sorted doubly linked list of distinct integers, find all triplets whose sum equals a given value in O(n²) time.
2. Build a simple text editor buffer using a doubly linked list of characters with a cursor, supporting `insert(char)`, `move_left()`, `move_right()`, `backspace()`, and `delete()` in O(1) each.
3. Add two numbers represented as doubly linked lists (head is the most significant digit) by using the `prev` pointers to add from the tail, without reversing either list.


# Today's Assignment — Circular Linked List

## 🟢 Basic (7)

1. Write a method `delete_at_position(index)` for a circular linked list, handling the head, the tail, and the single-node cases.
2. Write a method `insert_after_value(target, value)` for a circular linked list, making sure the tail's link is updated if `target` was the last node.
3. Implement a circular linked list that keeps only a `tail` pointer (so `tail.next` is the head), and support O(1) `insert_at_beginning()` and `insert_at_end()`.
4. Write a method `count_occurrences(value)` that returns how many times a value appears in a circular linked list.
5. Write a method `rotate_left(k)` that rotates the circular list by `k` positions by just moving the head pointer (no node data is changed).
6. Write a method `replace_all(old, new)` that replaces every occurrence of a value in a circular linked list.
7. Add `__len__` and `__iter__` (a generator that yields each node's data exactly once) to your circular linked list class.

## 🟡 Intermediate (5)

1. Check whether two circular linked lists represent the same cyclic sequence, regardless of their starting node (e.g., `1→2→3` and `3→1→2`).
2. Remove duplicate values from a circular linked list, keeping the first occurrence of each.
3. Delete every alternate node (the 2nd, 4th, 6th, ...) of a circular linked list in a single pass, and keep the list circular.
4. Insert a value into a sorted circular linked list so that it remains sorted (handle empty list, smaller-than-head, larger-than-tail, and middle cases).
5. Write a method `display_from(value)` that prints the entire circular list exactly once, starting from the node that holds the given value.

## 🔴 Advance (3)

1. Simulate the Clock (Second Chance) page replacement algorithm using a circular linked list with a "reference bit" per page and a moving clock hand.
2. Add two polynomials represented as circular linked lists (each node holds a coefficient and an exponent), returning the sum as a new circular linked list.
3. Check whether a circular linked list is a palindrome without using extra arrays: reverse the second half in place, compare, and then restore the original list.


# Today's Assignment — Stack

## 🟢 Basic (7)

1. Write a program to reverse every word in a sentence (but keep the word order) using a stack, e.g., `"I love Python"` → `"I evol nohtyP"`.
2. Implement a fixed-capacity `Stack` that raises a custom `StackOverflowError` when `push()` is called on a full stack.
3. Write a program to evaluate a prefix expression (e.g., `"+9*26"`) using a stack.
4. Write a program to find the "Previous Smaller Element" for every element in an array (the nearest smaller value to its left) using a stack.
5. Given two strings containing `#` as a backspace character, use a stack to check whether they are equal after typing (e.g., `"ab#c"` and `"ad#c"`).
6. Write a program to copy one stack into another while preserving the same order, using only stack operations.
7. Write a program to check whether the elements of a stack form a palindrome, using only stack operations (and no lists).

## 🟡 Intermediate (5)

1. Given a string of only `{` and `}`, find the minimum number of bracket reversals needed to make the expression balanced.
2. Simplify a Unix-style file path like `"/a/./b/../../c/"` into its canonical form (`"/c"`) using a stack.
3. Given a string of `(` and `)`, find the length of the longest valid (well-formed) parentheses substring using a stack.
4. Solve "Next Greater Element II": for a circular array, find the next greater element for each element, wrapping around the end.
5. Given a string and an integer `k`, repeatedly remove groups of `k` adjacent equal characters using a stack of (character, count) pairs (Remove All Adjacent Duplicates II).

## 🔴 Advance (3)

1. Solve "Remove Duplicate Letters": remove duplicate letters from a string so each letter appears once, and the result is the smallest in lexicographical order (monotonic stack).
2. Implement "Basic Calculator III": evaluate an expression containing digits, `+`, `-`, `*`, `/`, and parentheses using stacks, without `eval()`.
3. Compute the "Sum of Subarray Ranges" (sum of `max - min` over every contiguous subarray) in O(n) time using monotonic stacks.


# Today's Assignment — Queue

## 🟢 Basic (7)

1. Add `__len__`, `__iter__`, and `__str__` to your `Queue` class so that it works with `len()`, `for` loops, and `print()`.
2. Write a program to reverse a queue using a stack.
3. Write a program to find the sum, maximum, and minimum of a queue's elements without losing the original contents (by dequeuing and enqueuing each element back).
4. Write a program to check whether a queue is a palindrome using a deque.
5. Write a program that compares the time taken by `list.pop(0)` vs `collections.deque.popleft()` for 100,000 elements, and explain the difference.
6. Write a program to rotate a queue by `k` positions using only `enqueue()` and `dequeue()`.
7. Write a program to remove duplicate elements from a queue while preserving the order of first occurrence.

## 🟡 Intermediate (5)

1. Sort a queue using only queue operations and one extra queue (repeatedly find and move the minimum element).
2. Solve "Number of Students Unable to Eat Lunch": students in a queue prefer sandwiches (0/1) stacked in a pile; simulate the process and count who is left hungry.
3. Solve "Time Needed to Buy Tickets": given a queue of people who each want a number of tickets and buy one at a time, find how long a specific person takes.
4. Design a "Front Middle Back Queue" that supports `push_front`, `push_middle`, `push_back`, `pop_front`, `pop_middle`, and `pop_back` using two deques.
5. Solve "Dota2 Senate": use two queues to simulate a round-based voting game between two parties (`R` and `D`) and find the winning party.

## 🔴 Advance (3)

1. Solve "Word Ladder": given a begin word, an end word, and a dictionary, find the length of the shortest transformation sequence using BFS with a queue.
2. Implement topological sorting using Kahn's Algorithm (queue + in-degree array), and use it to solve "Course Schedule" (detect whether all courses can be finished).
3. Find the length of the longest subarray where the absolute difference between the maximum and minimum is at most `limit`, using two monotonic deques.
"""
