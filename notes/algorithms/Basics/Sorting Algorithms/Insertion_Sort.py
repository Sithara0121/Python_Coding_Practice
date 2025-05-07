def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be inserted
        j = i - 1
        # Shift elements to the right to make space for the key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insert the key at the correct position
    return arr

# Example usage
arr = [5, 1, 4, 2, 8]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)

# Logic:
# Insertion sort builds the sorted array one element at a time by inserting each element into its correct position.
# It compares the key element with the elements before it and shifts them to the right until the correct position is found.
# Example:
# Initial array: [5, 1, 4, 2, 8]
# After 1st pass: [1, 5, 4, 2, 8] (Insert 1 before 5)
# After 2nd pass: [1, 4, 5, 2, 8] (Insert 4 between 1 and 5)
# After 3rd pass: [1, 2, 4, 5, 8] (Insert 2 between 1 and 4)
# Time Complexity: Best case O(n) (if already sorted), Worst case O(n^2)
