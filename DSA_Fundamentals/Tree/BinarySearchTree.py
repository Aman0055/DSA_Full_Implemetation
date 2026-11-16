"""
Binary Search Tree

A binary search tree is the most important data structure that enables one to search for 
and find an element with an average running time :

f(n) = O(log₂ n)

Duplicate values are not allowed in BST (by default).

Diagram Of BINARY SEARCH TREE :
                                  50
                               /      \
                             30        70
                           /    \    /    \
                         10     40  60     80
                        /  \   / \  / \   / \
                       5   20 35 45 55 65 75 85

Binary Search Tree is a binary tree with the value of node N is greater than
every value in the left subtree of N and is less than every value in the right subtree of N.

Unless, explicitly said, BST don't allow duplicate values.

* Implementation : 
1> Node 2> Insertion 3> Traversing 4> Search 5> Deletion ::


                              Insertion

bst = BST()

70, 10, 25, 90, 60, 40, 100, 45  →  bst


                                  70
                                /    \
                              10      90
                                \       \
                                25      100
                                  \
                                  60
                                 /
                               40
                                 \
                                 45

                                 
            Traversing Preorder :

                                50
                              /    \
                            30      80
                           /  \    /  \
                         10   40  70   100


Preorder

Root → L → R

50 30 10 40 80 70 100

                              Inorder

                                50
                              /    \
                            30      80
                           /  \    /  \
                         10   40  70   100


Inorder Traversal

TL → root → TR

10 30 40 50 70 80 100


Inorder traversing of BST gives values in sorted order

                              Postorder

                                50
                              /    \
                            30      80
                           /  \    /  \
                         10   40  70   100


Postorder Traversal

TL → TR → root

10 40 30 70 100 80 50

① No child          10
② Single child      40
③ Two children      80


                              Deletion

                                  50
                                /    \
                              30      80
                             /  \    /  \
                           10   40  70   100
                                /   / \   / \
                               35  60 75 85 90
                                     /
                                    55
                                      \
                                      57


par ptr → 50
par ptr → 80

pred → 75
pred → 85
"""