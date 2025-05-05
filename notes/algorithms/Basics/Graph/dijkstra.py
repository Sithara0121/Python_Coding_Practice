import heapq

def dijkstra(graph, start):
    pq = [(0, start)]  # Priority Queue (min-heap) to store (distance, vertex)
    distances = {v: float('inf') for v in graph}  # Set all distances to infinity
    distances[start] = 0  # Distance to the start vertex is 0

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)  # Pop vertex with smallest distance

        # If a shorter distance has already been found for this vertex, skip it
        if current_distance > distances[current_vertex]:
            continue
        
        # Update distances for all neighbors
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))  # Push updated distance into the priority queue

    return distances

# Example usage:
g = {0: [(1, 1), (4, 1)], 1: [(0, 1), (4, 1), (2, 1)], 2: [(1, 1), (3, 1)], 3: [(2, 1)], 4: [(0, 1), (1, 1)]}
print(dijkstra(g, 0))

# Logic:
# Dijkstra's Algorithm finds the shortest path from a single source vertex to all other vertices in a graph with non-negative edge weights.
# It works by greedily choosing the vertex with the smallest tentative distance at each step.
# Time Complexity: O(V log V + E log V) using a priority queue (min-heap).
