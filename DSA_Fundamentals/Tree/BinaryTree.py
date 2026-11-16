"""
A Binary Tree is defined as a finite set of elements, called Nodes such that :
* T is empty (called the Null tree or Empty tree) or,
* T contains a distinguish node R, called the root of T, and the remaining nodes of T from an
    ordered  pair of disjoint binary trees T1 and T2.

                         Root node
                            ○
                           / \
                          /   \
                         ○     ○
                       /  \   /  \
                      /    \ /    \
                     ○     ○ ○     ○
                    / \   / \ / \   \
                   ○   ○ ○   ○ ○ ○   ○

<-------- Left Subtree Of Tree -------->
                                        <-------- Right Subtree Of Tree-------->


Any node in the binary tree has either
0, 1 or 2 child nodes.

                 Complete Binary Tree
                 ────────────────────

              All levels are completely filled.

                         ○
                       /   \
                      ○     ○
                    /  \   / \
                   ○    ○ ○   ○
                  
              L0 = 1
              L1 = 2
              L2 = 4
              L3 = 8
              L4 = 16
              L5 = 32
              L6 = 64
              L7 = 128
              Ln = 2ⁿ

         *       Almost Complete Binary Tree
                ────────────────────────────

All levels are completely filled, except
possibly the last level and nodes
in the last level are all left
aligned.


        ✗                         ○
                                /   \
                               ○     ○
                              / \
                             ○   ○

                  Strict Binary Tree
                  ──────────────────

Each node of a strict Binary Tree
will have either 0 or 2 children.

Full Binary Tree


                         ○
                       /   \
                      ○    ○
                          / \
                          ○   ○
                          / \
                         ○   ○

Representation of Binary Tree
──────────────────────────────

There are two possible representations
of binary tree

① Array Representation

② Linked Representation (by default)

                    Linked Representation
                    ──────────────────────

                         node
                          ↓
                 ┌───────────────────┐
                 │  left  │ item │ right │
                 └───────────────────┘


class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

                         Root
                         ────

                       root
                         ↓
                    ┌─────────────┐
                    │ left │ item │ right │
                    └─────────────┘


• root is a node pointer

• when root contains NULL, tree is empty.

                         root
                           ↓
                    ┌─────────────┐
                    │ left item right │
                    └─────────────┘
                      ↙          ↘
             ┌─────────────┐   ┌─────────────┐
             │ left item right │   │ left item right │
             └─────────────┘   └─────────────┘
                ↙        ↘          ↙
       ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
       │ left item right │ │ left item right │ │ left item right │
       └─────────────┘ └─────────────┘ └─────────────┘

                          Discuss
                          ────────

• How to insert an item in a BST?

• How to traverse a BT?


                            root
                             ↓
                            50
                          /    \
                        100     25
                               /
                              60

                             75

                             

                         50
                       /    \
                     20      30
                    /  \    /  \
      temp-  ----> 70   60  80  100
                          /  \
                        40    90
                              /
                            10

Code Execution for traverse :->
print(temp.item)        (50)
temp = temp.left
print(temp.item)        (20)
temp = temp.left
"""