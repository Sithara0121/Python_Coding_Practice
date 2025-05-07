# Question 4: Triplet Sum to Zero
# Problem: Given an array of integers, find all unique triplets in the array that sum to zero.
def triplet(nums):
  nums.sort()
  print(nums)
  result=[]
  for i in range(len(nums)):
    left=i+1
    right=len(nums)-1
    while left<right:
      if i==i+1:
        continue
      if(nums[left]+nums[right]==-(nums[i])):
        result.append([nums[left],nums[right],nums[i]])
      left+=1
      right-=1
  return result

triplet( [-1, 0, 1, 2, -1, -4])