def selectionSort(nums):
    # Traverse through all elements in the array
    for i in range(len(nums)):
        # Assume the minimum element is the first element in the unsorted part
        min_index = i
        
        # Find the minimum element in the unsorted part of the array
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
    
    return nums

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
