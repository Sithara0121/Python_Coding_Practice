def merge_sort(arr):
    if len(arr) <= 1:  # Base case: an array of length 0 or 1 is already sorted
        return arr
    mid = len(arr) // 2  # Find the middle of the array
    left_half = merge_sort(arr[:mid])  # Recursively sort the left half
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half
    return merge(left_half, right_half)  # Merge the sorted halves

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])  # Append remaining elements in left
    result.extend(right[j:])  # Append remaining elements in right
    return result

# Example usage
arr = [5, 1, 4, 2, 8]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)

# Logic:
# Merge sort divides the array into two halves, recursively sorts them, and then merges the sorted halves.
# The merging step combines two sorted lists into one sorted list by comparing the elements of both lists.
# Example:
# Initial array: [5, 1, 4, 2, 8]
# After splitting: [5, 1, 4] and [2, 8]
# After recursive sorting: [1, 4, 5] and [2, 8]
# After merging: [1, 2, 4, 5, 8]
# Time Complexity: O(n log n) for all cases
