def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Create empty buckets
    num_buckets = len(arr)
    min_val, max_val = min(arr), max(arr)
    bucket_range = (max_val - min_val) / num_buckets

    buckets = [[] for _ in range(num_buckets)]
    
    # Distribute the elements into buckets
    for num in arr:
        index = int((num - min_val) // bucket_range)
        if index == num_buckets:
            index -= 1
        buckets[index].append(num)
    
    # Sort each bucket and concatenate the result
    for i in range(num_buckets):
        buckets[i] = sorted(buckets[i])
    
    return [num for bucket in buckets for num in bucket]

# Example usage
arr = [0.42, 0.32, 0.65, 0.45, 0.23, 0.72, 0.12, 0.56]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)

# Logic:
# Bucket sort divides the range of input elements into several buckets, sorts each bucket individually, and then combines the buckets.
# It is most effective when the input data is uniformly distributed.
# Example:
# Initial array: [0.42, 0.32, 0.65, 0.45, 0.23, 0.72, 0.12, 0.56]
# Distribute into buckets and sort each: [0.12, 0.23, 0.32, 0.42, 0.45, 0.56, 0.65, 0.72]
# Time Complexity: Best case O(n + k), Worst case O(n^2) (if the data is not uniformly distributed)
