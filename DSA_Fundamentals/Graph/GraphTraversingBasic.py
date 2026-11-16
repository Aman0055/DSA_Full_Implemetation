"""
Graph Traversing ::::-->>>>

Agenda ::-->>
1> Traversing Graph
2> BFS
3> Logic Of BFS
4> Example
5> DFS
6> Logic Of DFS
7> Example 

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxTraversingxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
There are two standard way of traversing a Graph :

1> BFS -- Bredthe First Search
2> DFS == Depth First Search

Traversing graph has only issue that graph may have cycle. You may revisit a node.

To avoid processing a node more than once,  we divide the vertices into two category :->>
1> Visited 
2> Not Visisted

Note :-->>>  A boolean visited array is used to mark the visited vertices. 

BFS :-->> Breadthe First Search uses a queue data structure for traversal

Traversing began from a node called source Node.

Logic For BFS ::::

Let Q be the queue
Q.insert(s)
V[S] = True
while (!Q.isEmpty()):
{
n = Q.getFront()
Q.del()
for all the neighbours u of n 
    if v[u] == false
        Q.insert(u)
        v[u] = True
}

Diagram ::::::::::::::::-->>>>>>>>>>>>>>>>>>>

Source = V₀

                 Example
              ______________


          V₀          V₁          V₃          V₅
           ●───────────●───────────●───────────●
            ╲          │ ╲       ╱   ╲       ╱
             ╲         │  ╲     ╱     ╲     ╱
              ╲        │   ╲   ╱       ╲   ╱
               ╲       │    ╲ ╱         ╲ ╱
                ╲      │     ●───────────●
                 ╲     │    V₂          V₄


n = V₅


L₀ - V₀
L₁ - V₁
L₁ - V₂
L₂ - V₃
L₂ - V₄
L₃ - V₅


Q  [________________________________]


V       0    1    2    3    4    5
       ┌────────────────────────────┐
       │    T    T    T    T    T   T│
       └────────────────────────────┘

2> Depth First Search ::::::-->>

:- DFS is Depth First Search , The main difference between BFS and DFS is that 
the DFS uses STACK in place of QUEUE 
    
Note : Logic of DFS ::

DFS(G, S):
Let Stack be the Stack
stack.push(s)
v[s] = True
while (!stack.isEmpty())
{
n = stack.peek()
stack.pop()
for all the neighbours u of n 
    if v[u] == False
    stack.push(u)
    v[u] = True
}

Diagram :::::::::::::::---->>

Source = V₀

                 Example
              ______________


          V₀          V₁          V₃          V₅
           ●───────────●───────────●───────────●
            ╲          │ ╲       ╱   ╲       ╱
             ╲         │  ╲     ╱     ╲     ╱
              ╲        │   ╲   ╱       ╲   ╱
               ╲       │    ╲ ╱         ╲ ╱
                ╲      │     ●───────────●
                 ╲     │    V₂          V₄


n = V₁


L₀     V₀
L₁     V₂
L₂     V₄
L₃     V₅
L₂     V₃
L₁     V₁


        V
       ┌─────────────────────────┐
       │  0    1    2    3    4    5
       │  T    T    T    T    T    T
       └─────────────────────────┘
"""