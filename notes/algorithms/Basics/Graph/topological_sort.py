def topological_sort(graph):
    # Step 1: Compute in-degree of all vertices
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v, _ in graph[u]:
            in_degree[v] += 1
    
    # Step 2: Initialize the queue with vertices having in-degree 0
    queue = [u for u in in_degree if in_degree[u] == 0]
    sorted_order = []

    # Step 3: Process the vertices
    while queue:
        vertex = queue.pop(0)
        sorted_order.append(vertex)

        for neighbor, _ in graph[vertex]:
            in_degree[neighbor] -= 1  # Reduce in-degree of the neighbor
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if there is a cycle (i.e., if sorted order doesn't include all vertices)
    if len(sorted_order) != len(graph):
        print("Graph contains a cycle!")
        return None

    return sorted_order

# Example usage:
g = {0: [(1, 1)], 1: [(2, 1)], 2: [(3, 1)], 3: []}
print(topological_sort(g))

# Logic:
# Topological Sort is used to order the vertices of a Directed Acyclic Graph (DAG).
# The algorithm works by processing vertices with no incoming edges first and then removing them from the graph.
# It is useful for scheduling tasks, determining compilation order, and solving dependency problems.
# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
