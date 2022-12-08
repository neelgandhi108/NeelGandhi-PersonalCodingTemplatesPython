# Prefix Sum
1508. Range Sum of Sorted Subarray Sums

You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.

 

Example 1:

Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
Output: 13 
Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13. 


CODE

class Solution:
		def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
			ans = []
			prefix = [0]
			for num in nums:
				prefix.append(prefix[-1]+num)
			
			n = len(prefix)
			for i in range(1,n):
				for j in range(i-1,-1,-1):
					total = prefix[i] - prefix[j]
					ans.append(total)
			
			ans.sort()
			return sum(ans[left-1:right])
            
            
            
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

CODE

def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = {0:1}
        for n in nums:
            curSum += n
            diff = curSum -k
            res += prefixSums.get(diff,0)
            prefixSums[curSum] = 1+ prefixSums.get(curSum,0)
        return res