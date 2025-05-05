import heapq

def prim(graph):
    mst = []  # To store the edges of the MST
    visited = set()  # To track visited vertices
    min_heap = [(0, 0)]  # (weight, vertex) - start with any arbitrary vertex (vertex 0)

    while min_heap:
        weight, vertex = heapq.heappop(min_heap)  # Get the vertex with the minimum weight edge

        if vertex not in visited:
            visited.add(vertex)  # Mark the vertex as visited
            mst.append((vertex, weight))  # Add the edge to the MST

            # Add all unvisited neighbors to the priority queue
            for neighbor, edge_weight in graph[vertex]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor))

    return mst

# Example usage:
g = {0: [(1, 1), (2, 2)], 1: [(0, 1), (2, 1)], 2: [(0, 2), (1, 1)]}
print(prim(g))

# Logic:
# Prim's Algorithm finds the Minimum Spanning Tree (MST) of a connected, undirected graph with weighted edges.
# It starts with an arbitrary vertex, adds the minimum weight edge from the visited vertices to the MST, and repeats until all vertices are visited.
# Time Complexity: O(E log V) when using a priority queue (min-heap).
