#Floyd-Warshall Algorithm (All-Pairs Shortest Paths)
# This algorithm finds the shortest paths between all pairs of vertices in a weighted graph (with positive or negative weights, but no negative cycles).
def floyd_warshall(graph, vertices):
    # Step 1: Initialize the distance matrix with infinity and zero for diagonal
    dist = [[float('inf')] * vertices for _ in range(vertices)]
    
    for v in range(vertices):
        dist[v][v] = 0  # Distance from a vertex to itself is 0
    
    # Step 2: Set initial distances from the graph's edges
    for u in graph:
        for v, weight in graph[u]:
            dist[u][v] = weight
            dist[v][u] = weight  # For undirected graph
    
    # Step 3: Update the distance matrix by considering intermediate vertices
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example usage:
g = {0: [(1, 5), (2, 10)], 1: [(2, 2)], 2: [(0, 3), (1, 2)]}
vertices = 3
result = floyd_warshall(g, vertices)
for row in result:
    print(row)

# Logic:
# Floyd-Warshall algorithm computes the shortest paths between all pairs of vertices in a weighted graph.
# It works by iteratively improving the distance estimates by considering each vertex as an intermediate vertex.
# This algorithm is especially useful for graphs with negative weights but no negative-weight cycles.
# Time Complexity: O(V^3), where V is the number of vertices.
