import heapq

def heap_sort(arr):
    # Convert the list into a min-heap
    heapq.heapify(arr)
    sorted_arr = []
    
    # Pop the smallest element one by one
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    
    return sorted_arr

# Example usage
arr = [5, 1, 4, 2, 8]
sorted_arr = heap_sort(arr)
print("Sorted array:", sorted_arr)

# Logic:
# Heap sort uses a binary heap data structure. A binary heap is a complete binary tree that satisfies the heap property.
# The algorithm works by converting the input array into a heap, then repeatedly removing the smallest element.
# Example:
# Initial array: [5, 1, 4, 2, 8]
# After heapifying: [1, 2, 4, 5, 8] (heapify step)
# The smallest element is repeatedly popped: [1, 2, 4, 5, 8]
# Time Complexity: O(n log n) for both best and worst cases
