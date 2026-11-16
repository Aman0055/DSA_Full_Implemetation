"""
Tree :-> A tree is a defined as a finite set of one or more data items(nodes). such that,
        there is such a special node called the root node of the tree and the remaining nodes,
        are partitioned into n>= 0 disjoint subsets, each of which is itsself a tree, and they
        are known as subtree.

                T
                |
            Root node
            /       \
          T₁         T₂
        (Left)     (Right)
       Subtree     Subtree

* Subtrees :->

Root node: T
T₁ (T1): The left subtree of the root node.
T₂ (T2): The right subtree of the root node.

A subtree is a tree that consists of a node and all of its descendants.

In the diagram:

The complete tree is T.
The left portion is T₁.
The right portion is T₂.

Degree of the tree = 4     -->        
      ○  Root(2 Child)                                  Level(0)
    / | \
   /  |  \
  ○   ○   ○  (Edge, Subtree)                            Level(1)
 / \  |  /|\
○   ○ ○ ○ ○ ○ (LowerMost Nodes Of The SubTree)          Level(2)

Leaf Node or Terminal Node

Level 0
Level 1
Level 2

Level Number 0, 1 and 2

Generations 3

Parent-Child

 ○  Parent
 |
 ○  Child
"""