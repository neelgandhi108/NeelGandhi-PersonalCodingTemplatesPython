LeetCode 268 - Missing Number [easy]

Given an array containing n distinct numbers taken from 0, 1, 2, …, n, find the one that is missing from the array.

Example 1:

Input: [3, 0, 1]
Output: 2

CODE

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = 0

        while start < len(nums):
            num = nums[start]
            if num < len(nums) and num != start:
                nums[start], nums[num] = nums[num], nums[start]
            else:
                start += 1

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)