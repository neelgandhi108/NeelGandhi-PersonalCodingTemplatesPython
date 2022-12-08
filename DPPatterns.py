#Dynamic Programming

1)0/1 Knapsack

LeetCode 416 - Partition Equal Subset Sum [medium]

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100. The array size will not exceed 200.

Example 1:

Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

#Top-down Dynamic Programming with Memoization


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        
        if s % 2 != 0:
            return False
        
        # initialize two-dimensional dp array, -1 for default
        dp = [[-1 for x in range(int(s/2)+1)] for y in range(len(nums))]
        
        if self.can_partition_recursive(dp, nums, int(s / 2), 0) == 1:
            return True  # return True for 1
        else:
            return False  # return False for 0
        
    def can_partition_recursive(self, dp, nums, sum, current_index):
        if sum == 0:
            return 1
        
        if len(nums) == 0 or current_index >= len(nums):
            return 0
        
        if dp[current_index][sum] == -1:  # if we have not processed this sub-problem
                if nums[current_index] <= sum:
                    if self.can_partition_recursive(dp, nums, sum - nums[current_index], current_index + 1) == 1:
                        dp[current_index][sum] = 1
                        return 1

                # recursive call after excluding the number at the current_index
                dp[current_index][sum] = self.can_partition_recursive(dp, nums, sum, current_index + 1)

        return dp[current_index][sum]

#Bottom-up Dynamic Programming with Tabulation

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        
        if s % 2 != 0:
            return False
        
        s = int(s / 2)
        dp = [[False for x in range(s + 1)] for y in range(len(nums))]
        
        # populate s = 0 columns
        for i in range(0, len(nums)):
            dp[i][0] = True
            
        # form a subset only when the required sum is equal to its value
        for j in range(1, s + 1):
            dp[0][j] = nums[0] == j
        
        # process all subsets for all sums
        for i in range(1, len(nums)):
            for j in range(1, s + 1):
                # if we can get the sum 'j' without the number at index 'i'
                if dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][j]
                    
                # else if we can find a subset to get the remaining sum
                elif j >= nums[i]:
                    dp[i][j] = dp[i - 1][j - nums[i]]
        
        # the bottom-right corner will have our answer
        return dp[len(nums) - 1][s]
        
        
2)Staircase (DP)

LeetCode 70 - Climbing Stairs [easy]

You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note:

Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
--> 1 step + 1 step
--> 2 steps

Top-down Dynamic Programming with Memoization

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for x in range(n+1)]
        return self.climbStairs_recursive(dp, n)
    
    def climbStairs_recursive(self, dp, n):
        # we don't take any steps, so there is only 1 way
        if n == 0:
            return 0
        # we can take one step to reach the end, and this is the only way
        if n == 1:
            return 1
        # we can take one step twice or take two steps to reach the end
        if n == 2:
            return 2
        
        if dp[n] == 0:
            # if we take one step, we are left with "n - 1" steps
            take1step = self.climbStairs_recursive(dp, n - 1)
            # if we take two steps, we are left with "n - 2" steps
            take2steps = self.climbStairs_recursive(dp, n - 2)
            
            dp[n] = take1step + take2steps
            
        return dp[n]
        
Bottom-up Dynamic Programming with Tabulation

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for x in range(n+1)]
        dp[0] = 1
        dp[1] = 1

        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
        
        
3)Palindromes (DP)

LeetCode 516 - Longest Palindromic Subsequence [medium]

Given a string s, find the longest palindromic subsequence’s length in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "bbbab"
Output: 4
One possible longest palindromic subsequence is "bbbb".

Top-down Dynamic Programming with Memoization

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        return self.longestPalindromeSubseq_recursive(memo, s, 0, len(s) - 1)

    def longestPalindromeSubseq_recursive(self, memo, s, start, end):
        if start > end:
            return 0

        # every sequence with one element is a palindrome of length 1
        if start == end:
            return 1

        if memo[start][end] == -1:
            # case 1: elements at the beginning and the end are the same
            if s[start] == s[end]:
                memo[start][end] = 2 + self.longestPalindromeSubseq_recursive(memo, s, start + 1, end - 1)
            else:
                # case 2: skip one element either from the beginning or the end
                subseq1 = self.longestPalindromeSubseq_recursive(memo, s, start + 1, end)
                subseq2 = self.longestPalindromeSubseq_recursive(memo, s, start, end - 1)
                memo[start][end] = max(subseq1, subseq2)

        return memo[start][end]
        
Bottom-up Dynamic Programming with Tabulation

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = [[0 for _ in range(len(s))] for _ in range(len(s))]

        # every sequence with one element is a palindrome of length 1
        for i in range(len(s)):
            memo[i][i] = 1

        for start in range(len(s) - 1, -1, -1):
            for end in range(start + 1, len(s)):
                # case 1: elements at the beginning and the end are the same
                if s[start] == s[end]:
                    memo[start][end] = 2 + memo[start + 1][end - 1]
                else:  # case 2: skip one element either from the beginning or the end
                    memo[start][end] = max(memo[start + 1][end], memo[start][end - 1])

        return memo[0][len(s) - 1]
        
4)Longest Common Substring/Subsequence (DP)

LeetCode 1143 - Longest Common Subsequence [medium]

Given two strings text1 and text2, return the length of their longest common subsequence.

A common subsequence of two strings is a subsequence that is common to both strings. If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.


Top-down Dynamic Programming with MemoizationPermalink

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        return self.longestCommonSubsequence_recursive(memo, text1, text2, 0, 0)

    def longestCommonSubsequence_recursive(self, memo, text1, text2, i, j):
        if i == len(text1) or j == len(text2):
            return 0
        if memo[i][j] == -1:
            if text1[i] == text2[j]:
                memo[i][j] = 1 + self.longestCommonSubsequence_recursive(memo, text1, text2, i + 1, j + 1)
            else:
                memo[i][j] = max(self.longestCommonSubsequence_recursive(memo, text1, text2, i + 1, j),
                                 self.longestCommonSubsequence_recursive(memo, text1, text2, i, j + 1))
        return memo[i][j]
        
Bottom-up Dynamic Programming with Tabulation

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        max_length = 0
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

                max_length = max(max_length, memo[i][j])
        return max_length


