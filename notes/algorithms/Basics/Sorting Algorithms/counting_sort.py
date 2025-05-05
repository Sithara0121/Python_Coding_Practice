def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Store the count of each element
    for num in arr:
        count[num - min_val] += 1

    # Change count[i] to store the actual position of this number in output[]
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

# Example usage
arr = [5, 1, 4, 2, 8, 0, 2, 7]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)

# Logic:
# Counting sort counts the number of occurrences of each distinct element and uses this count to place each element in its correct position.
# Example:
# Initial array: [5, 1, 4, 2, 8, 0, 2, 7]
# Count the occurrences: [1, 1, 2, 1, 1, 1, 1, 1, 1]
# Rebuild the sorted array: [0, 1, 2, 2, 4, 5, 7, 8]
# Time Complexity: O(n + k), where n is the number of elements and k is the range of the input values
