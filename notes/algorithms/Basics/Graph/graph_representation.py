class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = {i: [] for i in range(vertices)}  # Adjacency list
    
    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))  # Add edge from u to v
        self.graph[v].append((u, weight))  # Add edge from v to u for undirected graph

    def __str__(self):
        return str(self.graph)

# Example usage:
g = Graph(5)  # Create a graph with 5 vertices
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 4)
g.add_edge(1, 2)
g.add_edge(2, 3)
print(g)

# Logic:
# The graph is represented as an adjacency list. Each vertex is associated with a list of tuples.
# Each tuple contains a neighboring vertex and the weight of the edge connecting them.
# Adjacency lists are space-efficient and faster for sparse graphs (few edges).
