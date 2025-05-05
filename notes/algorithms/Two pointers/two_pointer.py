# Two Pointer Pattern - Find two numbers in a sorted array that sum to a given target.

def two_pointer(arr, target):
    # Initialize two pointers
    left = 0
    right = len(arr) - 1

    # Iterate through the array until the left pointer crosses the right pointer
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return (arr[left], arr[right])  # Found the pair
        elif current_sum < target:
            left += 1  # Move left pointer to the right to increase sum
        else:
            right -= 1  # Move right pointer to the left to decrease sum
    
    return None  # Return None if no pair is found

# Example usage:
arr = [1, 3, 4, 6, 8, 9]
target = 10
result = two_pointer(arr, target)
print(result)  # Output: (1, 9)

# Logic:
# - Two pointers are used to traverse the sorted array from both ends.
# - Move the left pointer to the right or right pointer to the left depending on whether the sum is smaller or larger than the target.
# - Time Complexity: O(N) where N is the number of elements.
