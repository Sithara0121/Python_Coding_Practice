# Sliding window is used when you need to process a subset (window) of elements from a linear
# structure (like a list or string) and move that window efficiently.

# Instead of re-calculating things again and again, we slide a window and 
# update results incrementally, which leads to much faster performance.
# Use Sliding Window when:

# You're asked to find a subarray / substring / subset that meets a condition.

# The problem involves a fixed-size or dynamic-size window.

##Find the maximum sum of a subarray of size k.
def max_sum_subarray_k(arr, k):
    window_sum = sum(arr[:k])  # Sum of first window
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Slide the window
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray_k(arr, k))  
# Output: 9




