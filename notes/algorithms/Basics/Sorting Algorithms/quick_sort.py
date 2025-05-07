def quick_sort(arr):
    if len(arr) <= 1:  # Base case: an array of length 0 or 1 is already sorted
        return arr
    pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot
    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort and merge

# Example usage
arr = [5, 1, 4, 2, 8]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

# Logic:
# Quick sort uses a divide-and-conquer approach. It picks a 'pivot' element, and then divides the array into three parts:
# - Elements smaller than the pivot
# - Elements equal to the pivot
# - Elements greater than the pivot
# It then recursively sorts the left and right sub-arrays.
# Example:
# Initial array: [5, 1, 4, 2, 8]
# Pivot is 4, left of pivot = [1, 2], right of pivot = [5, 8]
# Recursively sorting sub-arrays: [1, 2], [5, 8] → Final result [1, 2, 4, 5, 8]
# Time Complexity: Best case O(n log n), Worst case O(n^2)
