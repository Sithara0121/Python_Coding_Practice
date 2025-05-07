def cycle_detection(graph):
    visited = set()

    def dfs(v, parent):
        visited.add(v)

        for neighbor, _ in graph[v]:
            if neighbor not in visited:
                if dfs(neighbor, v):
                    return True
            elif neighbor != parent:  # If an already visited vertex is not the parent, cycle exists
                return True
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, -1):
                return True
    return False

# Example usage:
g = {0: [(1, 1)], 1: [(0, 1), (2, 1)], 2: [(1, 1)]}  # No cycle
print(cycle_detection(g))  # Output: False

g = {0: [(1, 1)], 1: [(0, 1), (2, 1)], 2: [(1, 1), (0, 1)]}  # Contains a cycle
print(cycle_detection(g))  # Output: True

# Logic:
# Cycle detection in an undirected graph can be done using DFS with a parent pointer.
# During DFS traversal, if an adjacent vertex is visited and is not the parent of the current vertex,
# then a cycle is detected.
# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
