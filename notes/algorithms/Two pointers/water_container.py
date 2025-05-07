# Question 3: Container with Most Water
# Problem: You are given an array of integers where each element represents the height of a vertical line
#  drawn on a 2D plane. Find two lines, from the given array, 
# that together with the x-axis form a container, such that the container holds the most water.
#  Return the maximum amount of water it can contain.
def water_container(nums):
  right=len(nums)-1
  left=0
  length=0
  height=0
  volume=0
  while left<right:
    length=right-left
    height=min(nums[left],nums[right])
    volume=max(volume,length*height)
    if nums[left] < nums[right]:
            left += 1
    else:
            right -= 1
  return volume
print(water_container([1, 8, 6, 2, 5, 4, 8, 3, 7]))

# Output: 49