def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # For digits 0 to 9
    
    # Count occurrences of digits at current place (exp)
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Change count[i] to represent the actual position of this digit in the output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array
    for i in range(n-1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
    
    # Copy the output array to arr[], so that arr[] now contains sorted numbers based on current digit
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1  # Start with the least significant digit
    
    # Perform counting sort for every digit
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    
    return arr

# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print("Sorted array:", sorted_arr)

# Logic:
# Radix sort is a non-comparative sorting algorithm that processes the digits of the numbers.
# It sorts based on each digit starting from the least significant digit (LSD) or most significant digit (MSD).
# Example:
# Initial array: [170, 45, 75, 90, 802, 24, 2, 66]
# First pass (LSD): Sort by the least significant digit → [170, 802, 2, 24, 66, 45, 75, 90]
# Second pass: Sort by the second digit → [2, 24, 45, 66, 75, 90, 170, 802]
# Time Complexity: O(n * k), where n is the number of elements and k is the number of digits
