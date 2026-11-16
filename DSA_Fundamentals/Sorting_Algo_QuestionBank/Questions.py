"""
15 Practice Questions on Sorting Algorithms

Organized by difficulty and type so you can work through them progressively — conceptual 
understanding first, then tracing, then implementation, then deeper comparison/debugging.

Section A: Conceptual Understanding (Q1–Q4)

Q1. Explain in your own words why Bubble Sort is called "bubble" sort. What exactly moves 
toward its correct position on each pass — the largest or the smallest element 
(assuming ascending order)?

Q2. Selection Sort and Insertion Sort both have O(n²) time complexity, but they behave very 
differently in practice. Explain the core difference in how each one builds the sorted portion 
of the array.

Q3. Merge Sort and Quick Sort are both "divide and conquer" algorithms, yet one is called 
stable and reliably O(n log n), while the other's worst case is O(n²). Explain what causes 
this difference — specifically, what happens during the "divide" step of each.

Q4. What does it mean for a sorting algorithm to be stable? Give a concrete example with a 
small array of (key, value) pairs where stability would visibly matter, and state whether 
Bubble Sort, Insertion Sort, Selection Sort, Merge Sort, and Quick Sort 
(standard implementation) are stable or not.

Section B: Trace / Dry-Run by Hand (Q5–Q8)

Q5. Manually trace Insertion Sort on [9, 5, 1, 4, 3]. Write out the state of the array after 
each outer-loop iteration (i.e., after each new element is inserted into the sorted portion).

Q6. Manually trace Selection Sort on [64, 25, 12, 22, 11]. For each pass, state which minimum 
element was found and which two positions were swapped.

Q7. Manually trace Bubble Sort on [5, 1, 4, 2, 8], including the optimized version that stops 
early if no swaps occur in a pass. On which pass number does it terminate early, and why?

Q8. Manually trace Merge Sort on [38, 27, 43, 3, 9, 82, 10]. Draw (or describe in text) the
 recursive splitting tree down to single elements, then show each merge step back up.

Section C: Implementation / Coding (Q9–Q11)

Q9. Implement Quick Sort in Python using the Lomuto partition scheme (pivot = last element). 
Then implement it a second time using the Hoare partition scheme. Compare: which one does fewer
 swaps on average, and why?

Q10. Implement Merge Sort so that it sorts an array of custom objects (e.g., a list of 
Student(name, gpa) objects) by a given key function, similar to Python's sorted(arr, key=...). 
Your merge step must preserve stability.

Q11. Implement an in-place variant of Insertion Sort that works on a doubly linked list 
instead of an array. Why is this a more natural fit for a linked list than Selection Sort 
would be? (Hint: think about what operation each algorithm relies on most — shifting or 
searching.)

Section D: Complexity & Comparison (Q12–Q13)

Q12. Fill in this table from memory, then verify by reasoning through each algorithm 
(don't just memorize):

Algorithm	Best Case	Average Case	Worst Case	Space	Stable?	In-place?
Bubble Sort	?	?	?	?	?	?
Selection Sort	?	?	?	?	?	?
Insertion Sort	?	?	?	?	?	?
Merge Sort	?	?	?	?	?	?
Quick Sort	?	?	?	?	?	?

Q13. You're given an array that is already almost sorted (say, only 2–3 elements are out of 
place in an array of 10,000). Which of the five algorithms would you pick, and why? Which 
would you actively avoid, and why? Justify using time complexity, not just intuition.

Section E: Debugging / Edge Cases (Q14–Q15)

Q14. The following Quick Sort implementation has a subtle bug that causes infinite recursion
 on certain inputs (e.g., an array where all elements are equal). Find and fix it:

python
def quick_sort(arr, low, high):
    if low < high:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        pivot_index = i + 1
        quick_sort(arr, low, pivot_index)      # bug is here
        quick_sort(arr, pivot_index, high)      # and here

Q15. A Merge Sort implementation works correctly on arrays of even length but produces 
incorrect results (or crashes) on arrays of odd length. Given only that symptom, what part 
of the algorithm would you inspect first, and what's the most likely mistake? (You don't need
 to see the code — reason about where an odd-length array typically breaks a divide-and-conquer
   implementation.)
"""