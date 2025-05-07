def bellman_ford(graph, vertices, start):
    distances = {v: float('inf') for v in range(vertices)}  # Set initial distances to infinity
    distances[start] = 0  # Distance to the start vertex is 0

    # Relax all edges (vertices-1) times
    for _ in range(vertices - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:  # Relaxation step
                    distances[v] = distances[u] + weight

    # Check for negative-weight cycles
    for u in graph:
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                print("Graph contains negative weight cycle")
                return None

    return distances

# Example usage:
g = {0: [(1, 5), (2, 2)], 1: [(2, 1)], 2: [(3, 3)], 3: [(1, -6)]}
vertices = 4
print(bellman_ford(g, vertices, 0))

# Logic:
# Bellman-Ford algorithm is used for finding the shortest paths from a single source vertex to all other vertices, even with negative edge weights.
# Unlike Dijkstra, it can handle negative weight edges but is slower.
# It repeatedly relaxes all edges for V-1 iterations to ensure the shortest paths are found.
# Time Complexity: O(V * E), where V is the number of vertices and E is the number of edges.
