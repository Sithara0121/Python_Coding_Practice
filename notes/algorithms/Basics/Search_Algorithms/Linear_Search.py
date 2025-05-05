def linear_search(arr, target):
    # Loop through the list
    for i in range(len(arr)):
        if arr[i] == target:  # If target is found
            return i  # Return the index of the target
    return -1  # Return -1 if target is not found

# Example usage
arr = [10, 20, 30, 40, 50]
target = 30
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")
