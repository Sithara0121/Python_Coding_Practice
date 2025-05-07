def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume the min element is at i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:  # Find the smallest element
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the smallest element with the first unsorted element
    return arr

# Example usage
arr = [5, 1, 4, 2, 8]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)

# Logic:
# Selection sort repeatedly selects the minimum element from the unsorted part of the array and swaps it with the first unsorted element.
# It does this for every element, thereby gradually placing the smallest elements at the beginning.
# Example:
# Initial array: [5, 1, 4, 2, 8]
# After 1st pass: [1, 5, 4, 2, 8] (1 is the smallest element, swap with 5)
# After 2nd pass: [1, 2, 4, 5, 8] (2 is the smallest among remaining, swap with 5)
# Time Complexity: Best case O(n^2), Worst case O(n^2)
