def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(vertex)  # Mark the current vertex as visited
    print(vertex, end=" ")  # Process the current vertex (print it)

    # Recurse for each unvisited neighbor
    for neighbor, _ in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage:
g = {0: [(1, 1), (4, 1)], 1: [(0, 1), (4, 1), (2, 1)], 2: [(1, 1), (3, 1)], 3: [(2, 1)], 4: [(0, 1), (1, 1)]}
dfs(g, 0)

# Logic:
# DFS starts from a given vertex and explores as far as possible along each branch before backtracking.
# It's implemented using recursion, but can also be implemented using an explicit stack.
# It is useful for exploring all nodes in a connected component or checking if a graph is connected.
# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
