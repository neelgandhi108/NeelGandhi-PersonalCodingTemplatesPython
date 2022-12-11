1. Fibonacci Numbers
Climbing Stairs
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
		
House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
		
Fibonacci Number
Top-down Memoization

memo = {0: 0, 1: 1}

def fibonacci_memoization(n):
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
        return memo[n]

bottom-up approach is called Tabulation.

def fibonacci_tabulation(n):
    if n == 0:
        return n

	# pre-initialize array
    f = [0] * (n + 1)
    f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]
	
Maximum Alternating Subsequence Sum



2. Zero / One Knapsack
Partition Equal Subset Sum

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
        
Target Sum

494. Target Sum

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
                i + 1, total - nums[i]
            )
            return dp[(i, total)]

        return backtrack(0, 0)

3. Unbounded Knapsack
Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

Coin Change II

518. Coin Change II
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # MEMOIZATION
        # Time: O(n*m)
        # Memory: O(n*m)
        cache = {}

        def dfs(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]

            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]

        return dfs(0, 0)

        # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n*m)
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)
        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]

        # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n) where n = amount
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]
		
Minimum Cost for Tickets

4. Longest Common Subsequence
Longest Common Subsequence

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


Longest Increasing Subsequence
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing 
subsequence 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
		
Edit Distance

72. Edit Distance
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return dp[0][0]

Distinct Subsequences

115. Distinct Subsequences
Given two strings s and t, return the number of distinct 
subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        for i in range(len(s) + 1):
            cache[(i, len(t))] = 1
        for j in range(len(t)):
            cache[(len(s), j)] = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    cache[(i, j)] = cache[(i + 1, j + 1)] + cache[(i + 1, j)]
                else:
                    cache[(i, j)] = cache[(i + 1, j)]
        return cache[(0, 0)]

5. Palindromes
Longest Palindromic Subsequence


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
		
Palindromic Substrings
#https://leetcode.com/problems/palindromic-substrings/solutions/555333/python-dynamic-programming-solution/?orderBy=most_votes&languageTags=python
647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        
        # create a matrix to store info about the substring 
        dp = [[0 for i in range(n)] for j in range(n)]
        
        # set single characters as palindromes
        idx = 0
        while idx < n:
            dp[idx][idx] = 1
            idx += 1
            res += 1
        
        # fill the matrix 
        # example1: "aaaaa"
        # [1, 1, 1, 1, 1]
        # [0, 1, 1, 1, 1]
        # [0, 0, 1, 1, 1]
        # [0, 0, 0, 1, 1]
        # [0, 0, 0, 0, 1]
        
        # example2: "cdaabaad"
        # [1, 0, 0, 0, 0, 0, 0, 0]
        # [0, 1, 0, 0, 0, 0, 0, 1]
        # [0, 0, 1, 1, 0, 0, 1, 0]
        # [0, 0, 0, 1, 0, 1, 0, 0]
        # [0, 0, 0, 0, 1, 0, 0, 0]
        # [0, 0, 0, 0, 0, 1, 1, 0]
        # [0, 0, 0, 0, 0, 0, 1, 0]
        # [0, 0, 0, 0, 0, 0, 0, 1]
        
        for col in range(1, len(s)):
            for row in range(col):
                
                # every two chars are palindromes as well
                if row == col - 1 and s[col] == s[row]:
                    dp[row][col] = 1
                    res += 1
                
                # to determine if substring is a palindrome you should know 
                # a) if the inner substring is the palindrome and
                # b) if the outer characters match
                elif dp[row + 1][col - 1] == 1 and s[col] == s[row]:
                    dp[row][col] = 1
                    res += 1
        
        # print matrix
        # for line in dp:
        #     print(line)
        
        return res
		
Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res