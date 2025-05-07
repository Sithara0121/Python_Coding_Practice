#Question 1: Pair with a Given Sum
#Problem: Given a sorted array of integers, find two numbers that add up to a specific target.
# Return their indices or the numbers themselves.
def pair_sum(nums,target):
  left=0
  right=len(nums)
  while left<right:
    sum=nums[left]+nums[right-1]
    if(sum==target):
      return left,right
    elif sum<target:
      left+=1
    elif sum>target:
      right-=1
  return -1,-1

nums=[1,2,3,4,5,8,9,18,19,22]
print(pair_sum(nums,21))


#oputput: (1,9)