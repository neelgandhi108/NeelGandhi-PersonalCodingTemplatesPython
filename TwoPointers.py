Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].





CODE

#1
def twoSum(self, nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]

        if target > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum
    return [-1, -1]
	
#2
def twoSum(self, nums: List[int], target: int) -> List[int]:
    num_map = {}  # to store numbers and their indices
    for i, num in enumerate(nums):
        if target - num in num_map:
            return [num_map[target - num], i]
        else:
            num_map[nums[i]] = i
    return [-1, -1]