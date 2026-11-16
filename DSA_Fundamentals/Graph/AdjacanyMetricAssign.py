"""
Assignment-22: Adjacency Matrix implementation of Graph   
Write a class Graph to implement adjacency matrix representation of a simple and 
undirected graph.   
In class Graph, define __init__ method to initialise vertex_count and adj_matrix (list of lists)
In class Graph, define add_edge() method add an edge in the graph with given weight.
In class Graph, define remove_edge() method to remove an edge from the graph. 
In class Graph, define has_edge() method to check whether two given vertices are connected 
by an edge or not.
In class Graph, define print_adj_matrix() method to print adjacency matrix.   
"""
# Auto generated code for the Graph class with adjacency matrix representation :->
# class Graph:
#     def __init__(self, vertex_count):
#         self.vertex_count = vertex_count
#         self.adj_matrix = [[0 for _ in range(vertex_count)] for _ in range(vertex_count)]

#     def add_edge(self, u, v, weight=1):
#         if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
#             self.adj_matrix[u][v] = weight
#             self.adj_matrix[v][u] = weight  # For undirected graph

#     def remove_edge(self, u, v):
#         if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
#             self.adj_matrix[u][v] = 0
#             self.adj_matrix[v][u] = 0  # For undirected graph

#     def has_edge(self, u, v):
#         if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
#             return self.adj_matrix[u][v] != 0
#         return False

#     def print_adj_matrix(self):
#         for row in self.adj_matrix:
#             print(row)

"""
Diagram :-->> 

Graph
________

       V₀          V₁
        ●──────────●
                   / ╲
                  /   ● V₂
                 /    │
              ● V₃    │
               ╲      │
                ╲     ● V₄


V₀ : [ ]
V₁ : [ ]
V₂ : [ ]
V₃ : [ ]
V₄ : [ ]
"""

class Graph:
    def __init__(self, vno):
        self.vertex_count = vno
        self.adj_matrix = {v:[] for v in range(vno)}
    def add_edge(self, u, v, weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u].append((v, weight))
            self.adj_matrix[v].append((u, weight))
        else:
            print("Invalid vertices")
    def remove_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u] = [(vertices, weight) for vertices , weight in self.adj_matrix[u] if vertices != v]
            self.adj_matrix[v] = [(vertices, weight) for vertices, weight in self.adj_matrix[v] if vertices != u]
        else :
            print("Invalid Vertices !!")

    def has_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return any(vertices == v for vertices , x in self.adj_matrix[u])
        else :
            print("Invalid Vertices !!")
            return False
    def print_adj_list(self):
        for vertices, n in self.adj_matrix.items():
            print("V", vertices, ":", n)

obj = Graph(5)
obj.add_edge(0,1)
obj.add_edge(1,2)
obj.add_edge(1,3)
obj.add_edge(2,4)
obj.add_edge(3,4)
obj.print_adj_list()
    