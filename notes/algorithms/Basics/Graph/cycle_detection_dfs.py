def cycle_detection(graph):
    visited = set()
    recursion_stack = set()

    def dfs(v):
        if v in recursion_stack:  # If a vertex is in recursion stack, there is a cycle
            return True
        if v in visited:  # If a vertex is already visited, no cycle found
            return False

        visited.add(v)
        recursion_stack.add(v)

        for neighbor, _ in graph[v]:
            if dfs(neighbor):
                return True

        recursion_stack.remove(v)
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex):
                return True
    return False

# Example usage:
g = {0: [(1, 1)], 1: [(2, 1)], 2: [(3, 1)], 3: [(1, 1)]}  # Contains a cycle
print(cycle_detection(g))  # Output: True

# Logic:
# Cycle detection in a directed graph can be done using DFS by maintaining a recursion stack.
# If a node is encountered that's already in the recursion stack, a cycle is detected.
# This approach works well for detecting cycles in directed graphs.
# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
