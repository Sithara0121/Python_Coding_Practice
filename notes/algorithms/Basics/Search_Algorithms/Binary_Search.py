def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle element
        if arr[mid] == target:  # If target is found
            return mid
        elif arr[mid] < target:  # If target is greater, search the right half
            low = mid + 1
        else:  # If target is smaller, search the left half
            high = mid - 1
    return -1  # If target is not found

# Example usage
arr = [10, 20, 30, 40, 50]
target = 30
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")
