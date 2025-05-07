# working with contiguous elements, but this time  don’t know the window size 
# — so we dynamically expand and shrink the window:

# Expand the window until the sum ≥ target.

# Then shrink it from the left to find the smallest size possible.
# Problem
# Given an array of positive integers and a target sum s,
#  return the length of the smallest contiguous subarray whose sum is greater than or equal to s.
# If there isn’t one, return 0 instead.
def min_subarray_len(s, arr):
    window_start = 0
    window_sum = 0
    min_length = float('inf')

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # Expand the window

        # Shrink the window from the left while the condition is met
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    return min_length if min_length != float('inf') else 0

# Example usage
s = 7
arr = [2, 3, 1, 2, 4, 3]
print(min_subarray_len(s, arr))  # Output: 2


# - Start with window_start at 0 and increase window_end step by step.
# - As we add elements, if window_sum ≥ s, we try to shrink the window.
# - Keep tracking the smallest window that meets the condition.
# Time Complexity: O(N)

