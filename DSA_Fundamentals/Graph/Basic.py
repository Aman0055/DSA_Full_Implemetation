"""
Agenda for Graph :::
1.Graph :-> A graph is a non-linear data structure consisting of nodes(vertices) and edges. 
2.Adjacent of a node :-> The nodes which are connected to a given node by an edge are 
called adjacent nodes.
3.Degree of a node :-> The number of edges incident on a node is called the degree of the node.
4.Path :-> A path in a graph is a sequence of vertices such that from each of its vertices 
there is an edge to the next vertex in the sequence.
5.Connected Graph :-> A graph is said to be connected if there is a path between every pair 
of vertices.
6.Labbeled and Weight Graph :-> A graph is said to be labelled if each of its vertices is 
assigned a unique label. A graph is said to be weighted if each of its edges is assigned a
 weight.
7.Mulgraph and Directed Graph :-> A graph is said to be a multigraph if it has multiple edges 
between the same pair of vertices. A graph is said to be directed if its edges have a 
direction associated with them.
8.Complete Graph :-> A graph is said to be complete if there is an edge between every pair 
of vertices.
9.Representation of Graph :-> A graph can be represented in two ways, Adjacency Matrix and 
Adjacency List.

                         Graph
                         _____

• Graph is a non linear data
  structure


                              e₀ = [v₀, v₁]
                              e₁ = [v₁, v₂]

       v₀                         v₁                         v₃
       ●────────────── e₀ ───────●────────────── e₂ ───────●
                                  ╲                         |
                                   ╲ e₁                     |
                                    ╲                       |
                                     ● v₂
                                     │                      |
                                     │                      |
                                     └────────── e₃ ─────────● v₄
                                                               ╲
                                                                ╲ e₄
                                                                 ╲
                                                                  ●
                                                                  v₃


V = {v₀, v₁, v₂, v₃, v₄}

E = {e₀, e₁, e₂, e₃, e₄}

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx(Graph)xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
:- A Graph consist of two things 
:- A Set V  of elements called nodes.
:- A Set E of edges such that edge e in E is identified with a uniquie (unordered) pair
    [u, v] of nodes in v, denoted by e = [u, v] and called the endpoints of e. 
    We indicate the parts of Graph by writing G(V,E)

                                ***Adjacent Nodes***
:- If e = [u, v] then u and v are called adjacent nodes or neighbors
                    u .___________________________. v


                            ****Degree-Of-Nodes****
:- The degree of a node u, written deg(u), in the number of edges containing u.

If deg(u) = 0, then u is called an isolated node.


                                    ***Path***
:- A path of length n from a node u to node v is defined as sequence of n+1 nodes.
            p = (vo, v₁, v₂, v₃, ……, vn)
                                    u = v₀, v₁, v₂, v₃, ……, vn = v  
    :- The path p is said to be simple if all the nodes in the path are distinct.
    Eg : vo = vn 


                         Simple & Complex Path
                         ______________________


The path is said to be simple if
all the nodes are distinct, with the
exception that V₀ may equal to Vₙ
otherwise it is complex path.


                                  V₁                    V₄
                                ●════════════════════════●
                              ╱ ╲                        ╱
                            ╱     ╲                    ╱
                          ╱         ╲                ╱
                       V₀            ● V₃──────────● V₅
                                      ╲             ╱
                                       ╲           ╱
                                        ╲─────────╱
                                           
                                  ╲──────────────╱
                                      V₂


                                      V₀ V₁ V₄ V₃
                                      V₁ V₂ V₅ V₃


                         Connected Graph
                         ______________


A graph is said to be connected
if there is a path between any
two of its nodes.



        ●
       ╱
      ╱
     ●
      │
      │
      ●──────────────●──────────────●
                     ╲
                      ╲
                       ●


                    *** Tree Graph ***     
                         Tree Graph
                         __________


A connected graph T without any
cycles is called a tree graph or
free tree, or simply a tree.


This means in particular that
there is a unique simple path
P between any two nodes u and v.


                              ●
                             / \
                            /   \
                   ●───────●     ●────────●


                         Labelled Graph
                         ______________


A graph is to be labelled if its
edges are assigned data.



       P                 P                 P        P        P
●────────────●────────────●────────────●────────────●────────●
             ╲ B          ╲ Y
              ╲             ╲
               ╲             ●
                ╲           / \
                 ╲         /   \
                  ●───────●     ●
                  B       Y     Y
                  ╲       ╲     ╲
                   ╲       ╲     ╲
                    ●       ●─────●
                     ╲       Y
                      ╲
                       ●
                        B
                         ╲
                          ●


                         Weighted Graph
                         ______________


A graph G is said to be weighted
if each edge e in G is assigned
a non-negative numerical value w(e)
called the weight or length of e.



                         41
                    ●──────────●
                   /            ╲
                  /              ╲ 130
                 ●                ●────────●
                  ╲              /           20
                   ╲ 105        / 60
                    ╲          /
                     ╲        /
                      ●──────●


                      =========Loop============
:- An edge is called loop if it has a identical end points.

Eg : e = [u, u] is a loop edge.


                         Multi Graph
                         ___________


Multi Graph is a graph consisting
of multiple edges and loops.



             ●
              \
               \
                \
                 ●════════════●
                  ╲          ╱ \
                   ╲________╱   ╲
                                ╲
                                 ●
                                ╱╲
                               ╱  ╲
                              ╲    ╱
                               ╲__╱


                         Multi graph
                         ___________


                         Directed Graph
                         ______________

A directed graph G also called digraph
is same as multigraph except that
each edge e is assigned a direction.


                         e = (u, v)
                              ↑
                         ordered pair


                    u ──────→ v
                           e


                         ↗─────↘
                       ↙         ↘
                      ●           ●
                       ↖         ↙
                         ↖─────↙


                         @ Complete Graph

:- A simple graph in which there exists an edge between every pair of 
vertices called a complete graph. A complete graph with n vertices is denoted by Kₙ.
It is also known as universal graph or clique graph.

                         Graph
                         ______

                    v₁
                   / | \
                  /  |  \
                 /   |   \
               v₀────|────v₂
                |\    |   /|
                | \   |  / |
                |  \  | /  |
                |   \ |/   |
                |    \     |
                |     \    |
                |      \   |
                |       \  |
                |        \ |
                v₄────────v₃


                 Adjacency Matrix Representation
                 ________________________________

Suppose G is a simple graph with m nodes,
and suppose the nodes of G have been
ordered and are called v₁ v₂ v₃ ... vₘ. Then
the adjacency matrix A = (aᵢⱼ) of the
graph Gᵢ is the m × m matrix defined as
follows:

                         ⎧  1    if vᵢ is adjacent to vⱼ
                    aᵢⱼ = ⎨
                         ⎩  0    otherwise



                        *******Adjacency List Representation*****   
The adjacency list stores information about only those edges that exists.
The adjacency list contains a directory (dict) containing adjacency list for each vertex.  


"""