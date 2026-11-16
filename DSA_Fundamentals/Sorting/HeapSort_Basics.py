"""
Note : Before looking into the heap sort firstly go through the core concepts of complete
Binart Tree :::::::::::::::::::::::::

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxAgendaxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
1. Complete Binary Tree
2. Almost Complete Binary Tree
3. Heap
4. Insertion in Heap
5. Deletion in Heap
6. Heap Sort



              Complete Binary Tree

L0  ────→          ○
                  /   \
L1  ────→        ○     ○
                / \   / \
L2  ────→      ○   ○ ○   ○


All levels must be
completely filled.

L0  →  1
L1  →  2
L2  →  4
L3  →  8
L4  →  16
Ln  =  2ⁿ



          Almost Complete Binary Tree

                    ○
                  /   \
                ○       ○
              /   \   /   \
            ○     ○ ○     ○
           / \
          ○   ○


All the levels must be
completely filled except
possibly the last level
and all the nodes in the
last level must be left
aligned

=======================================Heap=====================================
Heap is a Data Structure , Heap is used in a sorting algorithm known as Heap Sort.
Heap are of two types :
1. Max Heap (Default)
2. Min Heap

xxxxxxxxxxxxxxxxxxxxxxxxxxx ---- Heap Propertities --- xxxxxxxxxxxxxxxxxxxxxxxxxxx
The value at Node N is greater than or equal to value at each children of Node N.

* Heap must be an almost complete binary tree :
By Default : n0 >= n1 and n0 >= n2 (This is a max heap)

* For min Heap :-->> n0 <= n1 and n0  <= n2


                         Example

              50                         40
             /  \                       /  \
           40    30                   10    30
          / \   /  \                       /  \
        20  30 10  25                   10    20
       / \                               / \
      5  10                             5   2


          Max-heap                 Not a heap

        xxxxxxxxxxxxx Representation of Heap xxxxxxxxxxxxxxxxxxx

Unless otherwise stated, heap is maintained
in memory by a linear array (list).


              50
             /  \
           40    30
          / \   /  \
        20  30 10  25
       / \
      5  10


H = [50, 40, 30, 20, 30, 10, 25, 5, 10]
     ────────────────────────────────────
Index:  0   1   2   3   4   5   6   7   8

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

                How to find parent or child node?

                              H
          0     1     2     3     4     5     6     7     8
        ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
        │ 50  │ 40  │ 30  │ 20  │ 30  │ 10  │ 25  │  5  │ 10  │
        └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘


                         50 (0)
                        /       \
                    40 (1)      30 (2)
                   /    \       /    \
              20 (3)  30 (4) 10 (5) 25 (6)
              /   \
           5 (7) 10 (8)


How to find index of child nodes?

index is index of node N

index of left child  = 2 * index + 1

index of right child = 2 * index + 2


How to find index of parent node?

index of node N = index

index of parent node of N = (index - 1) / 2


xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxInsertionxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Index:  0   1   2   3   4   5   6   7   8
      ┌───┬───┬───┬───┬───┬───┬───┬───┬───┐
      │40 │70 │10 │90 │60 │30 │50 │20 │80 │
      └───┴───┴───┴───┴───┴───┴───┴───┴───┘

H = [90, 80, 50, 70, 60, 10, 30, 20, 40]

Index:  0   1   2   3   4   5   6   7   8
      ┌───┬───┬───┬───┬───┬───┬───┬───┬───┐
      │90 │80 │50 │70 │60 │10 │30 │20 │40 │
      └───┴───┴───┴───┴───┴───┴───┴───┴───┘


                       90
                     /    \
                   80      50
                  /  \    /  \
                70   60  10   30
               /  \
             20    40

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxDeletionxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Note :->>> Heap Sort :-->>
                            Delete values from the heap(max-heap) and store them in an array
                            from right to left. As a result, at the end of deleting all the
                            elements of heap , array become sorted .

                            Heap can we used to impliment Priority Queue .

 """