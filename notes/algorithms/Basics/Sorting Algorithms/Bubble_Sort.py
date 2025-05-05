def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:  # Compare adjacent elements
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap if out of order
    return arr

# Example usage
arr = [5, 1, 4, 2, 8]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)


#note
# Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the

# Bubble Sort Algorithm
# Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

# How it works:
# Compare each pair of adjacent elements.

# Swap them if they are in the wrong order.

# Repeat the process for each element, reducing the number of comparisons after each iteration.

# Example:
# For the list [5, 1, 4, 2, 8], bubble sort will:

# Compare 5 and 1 (swap them),

# Compare 5 and 4 (swap them), and so on, until the list is sorted.
# Time Complexity:
# Best case: O(n) (if the array is already sorted).

# Worst case: O(n^2) (for a reverse-sorted array).

# Space Complexity: O(1), as bubble sort is an in-place algorithm.