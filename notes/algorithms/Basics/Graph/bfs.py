from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])  # Initialize queue with the start vertex
    visited.add(start)  # Mark start vertex as visited

    while queue:
        vertex = queue.popleft()  # Dequeue a vertex
        print(vertex, end=" ")  # Process the current vertex (print it)

        # Add all unvisited neighbors to the queue
        for neighbor, _ in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage:
g = {0: [(1, 1), (4, 1)], 1: [(0, 1), (4, 1), (2, 1)], 2: [(1, 1), (3, 1)], 3: [(2, 1)], 4: [(0, 1), (1, 1)]}
bfs(g, 0)

# Logic:
# BFS explores the graph level by level. It starts from the root node, visiting all neighbors,
# then moves on to the neighbors' neighbors, and so on.
# It uses a queue to ensure that nodes are visited in the correct order.
# BFS is often used for finding the shortest path in unweighted graphs or for exploring a graph's connectivity.
# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
