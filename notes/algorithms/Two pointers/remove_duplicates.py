# Question 2: Remove Duplicates from Sorted Array
# Problem: Given a sorted array, remove the duplicates in-place such that each element appears only once. 
# You must return the new length of the array after removing duplicates.
def remove_duplicates(arr):
  left=0
  for right in range(1,len(arr)):
    if arr[right]>arr[left]:
      left+=1
      arr[left]=arr[right]
  return arr[:left+1]

print(remove_duplicates([1,1,2,3,3,4,4,4,5,6,6,6,6,6,6,6,6,7,7,7,8,8,]))


# Output: [1, 2, 3, 4, 5, 6, 7, 8]

