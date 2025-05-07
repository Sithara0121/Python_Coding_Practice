class UnionFind:
    def __init__(self, vertices):
        # Initialize parent and rank for each vertex
        self.parent = {i: i for i in range(vertices)}  # Each vertex is its own parent initially
        self.rank = {i: 0 for i in range(vertices)}  # Rank (or depth) to keep the tree flat

    def find(self, u):
        # Find the root of the set containing u, with path compression
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        # Union by rank: Attach the smaller tree under the root of the larger tree
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u  # Make root_u the parent of root_v
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v  # Make root_v the parent of root_u
            else:
                self.parent[root_v] = root_u  # Arbitrary choice if ranks are equal
                self.rank[root_u] += 1  # Increment the rank of the root

def kruskal(graph, vertices):
    # Step 1: Sort all the edges in non-decreasing order of their weights
    edges = []
    for u in graph:
        for v, weight in graph[u]:
            edges.append((weight, u, v))  # Store edges as (weight, u, v)
    edges.sort()  # Sort edges based on the weight

    # Step 2: Create a UnionFind instance
    uf = UnionFind(vertices)
    mst = []  # To store the edges of the MST

    # Step 3: Iterate through the sorted edges and add them to the MST if they don't form a cycle
    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):  # If u and v are not in the same set, add edge to MST
            uf.union(u, v)
            mst.append((u, v, weight))  # Include the edge in the MST

    return mst

# Example usage:
# The graph is represented as an adjacency list (undirected graph).
# Each edge is represented as (u, v, weight), where u and v are vertices, and weight is the edge's weight.
g = {0: [(1, 10), (2, 6), (3, 5)],
     1: [(0, 10), (3, 15)],
     2: [(0, 6), (3, 4)],
     3: [(0, 5), (1, 15), (2, 4)]}

vertices = 4  # Number of vertices in the graph
mst = kruskal(g, vertices)
print("Minimum Spanning Tree (MST):")
for edge in mst:
    print(edge)

# Logic:
# Kruskal's Algorithm sorts all the edges in non-decreasing order of their weights.
# It then adds the smallest edge to the MST, provided it doesn't form a cycle (i.e., both vertices are not in the same set).
# The UnionFind data structure is used to efficiently track and merge sets of vertices.
# The algorithm ensures the MST is constructed in a greedy manner, always picking the smallest available edge that doesn't form a cycle.
# Time Complexity: O(E log E + E log V), where E is the number of edges and V is the number of vertices.
