def heapify(arr, n, i):
    largest = i          # Initialize largest as root
    left = 2 * i + 1     # Left child
    right = 2 * i + 2    # Right child

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not the largest, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

def heap_sort(arr):
    n = len(arr)

    # Build a max-heap (bottom-up approach)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap root (max) with last item
        heapify(arr, i, 0)               # Heapify the reduced heap

# Example usage
arr = [5, 1, 4, 2, 8]
heap_sort(arr)
print("Sorted array:", arr)

# Logic:
# 1. Build a max-heap from the input array.
# 2. Swap the root (largest) with the last element.
# 3. Reduce the heap size by 1 and heapify the root.
# 4. Repeat until the heap size is 1.
# This results in a sorted array in ascending order.

# Time Complexity:
# Best Case: O(n log n)
# Worst Case: O(n log n)
# Average:    O(n log n)
